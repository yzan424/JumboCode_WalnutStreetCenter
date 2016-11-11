from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from nutzserver.models import *
from django.template import *
import json, requests
import datetime

from PyPDF2 import PdfFileWriter, PdfFileReader
from io import StringIO
from io import BytesIO 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

backendGET = 'http://127.0.0.1:5000/api/patient/'
backendPOST = 'http://127.0.0.1:5000/api/patient/'
backendPUT = 'http://127.0.0.1:5000/api/patient/'


def profile(request, profile_id, edit):
    medical_info = requests.get(backendGET + profile_id + '/medical_info').json()
    basic_info = requests.get(backendGET + profile_id + '/basic_info').json()
    self_preservation = requests.get(backendGET + profile_id + '/self_preservation').json()
    identifying = requests.get(backendGET + profile_id + '/identifying_info').json()
    legal_guardian = requests.get(backendGET + profile_id + '/legal_guardian').json()

    full_result = requests.get(backendGET + profile_id)
    if not full_result:
        return HttpResponseNotFound('<h1>Profile not found</h1>')
    else:
        full_result = full_result.json()
    firstname = full_result.get('name_first') or ""
    lastname = full_result.get('name_last') or ""

    context_data = {'first_name': firstname,
                    'last_name': lastname,
                    'medical_info': medical_info,
                    'basic_info': basic_info,
                    'self_preservation': self_preservation,
                    'identifying': identifying,
                    'legal_guardian': legal_guardian,
                    'profile_id': profile_id}

    if not edit:
        return render(request, "profile.html", context=context_data)
    else:
        return render(request, "update_profile.html", context=context_data)


def protocol(request, profile_id, edit):
    protocols = requests.get(backendGET + profile_id + '/protocols')
    isp = requests.get(backendGET + profile_id + '/isp')
    supportive = requests.get(backendGET + profile_id + '/supportive')
    tracking = requests.get(backendGET + profile_id + '/tracking')  

    full_result = requests.get(backendGET + profile_id)
    full_result = full_result.json()
    firstname = full_result['name_first']
    lastname = full_result['name_last']

    protocols = protocols.json()
    # protocols = protocols['objects']
    isp = isp.json()
    supportive = supportive.json()
    # supportive = ['objects']
    tracking = tracking.json()
    # tracking = tracking['objects']

    if edit== False:
        return render(request, "protocol.html", context={'first_name': firstname, 'last_name': lastname, 'protocols': protocols, 'isp': isp, 'supportive': supportive, 'tracking': tracking, 'profile_id': profile_id})
    else:
        return render(request, "update_protocol.html", context={'first_name': firstname, 'last_name': lastname, 'protocols': protocols, 'isp': isp, 'supportive': supportive, 'tracking': tracking, 'profile_id': profile_id})        

def behavior(request, profile_id, edit):
    print(profile_id)
    medical_treatment_plan = requests.get(backendGET + profile_id + '/medical_treatment_plan')
    behavior = requests.get(backendGET + profile_id + '/behavior')
    behavior_support_plans = requests.get(backendGET + profile_id + '/behavior_support_plan')
    # restrictive = requests.get(backendGET + profile_id + '/restrictive')
    rogers_monitor = requests.get(backendGET + profile_id + '/rogers_monitor')

    full_result = requests.get(backendGET + profile_id)
    full_result = full_result.json()
    firstname = full_result['name_first']
    lastname = full_result['name_last']

    medical_treatment_plan = medical_treatment_plan.json()
    behavior = behavior.json()
    behavior_support_plans = behavior_support_plans.json()
    # restrictive = restrictive.json()

    #restrictive = restrictive['objects']
    rogers_monitor = rogers_monitor.json()
        
    if edit == False:
        return render(request, "behavior.html", context={'first_name': firstname, 'last_name': lastname, 'medical_treatment_plan': medical_treatment_plan, 'behavior': behavior, 'behavior_support_plan': behavior_support_plans, 'rogers_monitor': rogers_monitor, 'profile_id': profile_id})
    else:
        return render(request, "update_behavior.html", context={'first_name': firstname, 'last_name': lastname, 'medical_treatment_plan': medical_treatment_plan, 'behavior': behavior, 'behavior_support_plan': behavior_support_plans, 'rogers_monitor': rogers_monitor, 'profile_id': profile_id})        

def support(request, profile_id, edit):
    legal_guardian = requests.get(backendGET + profile_id + '/legal_guardian')
    insurance = requests.get(backendGET + profile_id + '/insurance')
    legal_status = requests.get(backendGET + profile_id + '/legal_competency')

    full_result = requests.get(backendGET + profile_id)
    full_result = full_result.json()
    firstname = full_result['name_first']
    lastname = full_result['name_last']

    legal_guardian = legal_guardian.json()
    insurance = insurance.json()
    # insurance = insurance['objects']
    legal_status = legal_status.json()
    # legal_status = legal_status['objects']
        
    if edit == False:
        return render(request, "support.html", context={'first_name': firstname, 'last_name': lastname, 'legal_guardian': legal_guardian, 'insurance': insurance, 'legal_status': legal_status, 'profile_id': profile_id})
    else:
        return render(request, "update_support.html", context={'first_name': firstname, 'last_name': lastname, 'legal_guardian': legal_guardian, 'insurance': insurance, 'legal_status': legal_status, 'profile_id': profile_id})        

def edit(request, page, profile_id):
    if page == 'profile':
        if request.method == 'GET':
            return profile(request, profile_id, True)
        else:
            # send the new stuffs to the backend
            updated_medical_info = {}
            updated_basic_info = {}
            updated_self_preservation = []
            new_self_preservation = []
            updated_identifying = {}
            updated_legal_guardian = {}

            for keys, values in request.POST.items():
                if (keys.split('.'))[0] == "basic_info":
                    updated_basic_info[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "medical_info":
                    updated_medical_info[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "identifying":
                    updated_identifying[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "legal_guardian":
                    updated_legal_guardian[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "self_preservation":
                    print(keys)
                    print(values)
                    self_preservation_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        print("existing")
                        #these are just edits to existing things
                         #create a new dictionary if it does not exist
                        if not any(x['id'] == self_preservation_id for x in updated_self_preservation):
                            updated_self_preservation.append({'id': self_preservation_id})

                        for i in updated_self_preservation:
                            if i['id'] == self_preservation_id:
                                i[dictKey] = values
                    else:
                        # new entries to self_preservation
                        # check if theres even anything in them
                        if values != '':
                            # these are just edits to existing things
                            if not any(x['id'] == self_preservation_id for x in new_self_preservation):
                                new_self_preservation.append({'id': self_preservation_id})

                            for i in new_self_preservation:
                                if i['id'] == self_preservation_id:
                                    i[dictKey] = values


            for i in updated_self_preservation:
                i['patient_id'] = profile_id

            print(updated_self_preservation)
            header = {'Content-Type': 'application/json'}
            updated_basic_info = json.dumps({"basic_info" : updated_basic_info})
            updated_identifying = json.dumps({"identifying_info" : updated_identifying})
            updated_medical_info = json.dumps({"medical_info" : updated_medical_info})
            updated_legal_guardian = json.dumps({"legal_guardian" : updated_legal_guardian})
            updated_self_preservation = json.dumps({"self_preservation" : updated_self_preservation})

            # send all the new stuff
            requests.put(backendPOST + profile_id, data=updated_identifying, headers=header)
            requests.put(backendPOST + profile_id, data=updated_medical_info, headers=header)
            requests.put(backendPOST + profile_id, data=updated_basic_info, headers=header)
            #requests.put(backendPOST + profile_id, data=updated_legal_guardian, headers=header)
            requests.put(backendPOST +  profile_id, data=updated_self_preservation, headers=header)

            print(updated_self_preservation)
            
        """ for i in updated_self_preservation:
                requests.put(spPOST, data=i)           
                i['patient_id'] = profile_id
                i = json.dumps(i)
                requests.post(spPOST, data=i, headers=header)
            for i in new_self_preservation:
                del i['self_preservation_id']
                i['patient_id'] = profile_id
                i = json.dumps(i)
                requests.post(spPOST, data=i, headers=header) """

        return HttpResponseRedirect("/profile/" + profile_id)
    elif page == "protocol":
        if request.method == "GET":
            return protocol(request, profile_id, True)
        else:
            print(request.POST)
            print('\n')
            updated_protocols = []
            new_protocols = []
            updated_isp = {}
            updated_supportive = []
            new_supportive = []
            updated_tracking = []
            new_tracking = []

            for keys, values in request.POST.items():
                if (keys.split('.'))[0] == "protocols":
                    protocols_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['protocols_id'] ==  protocols_id for x in updated_protocols):
                            updated_protocols.append({'protocols_id': protocols_id})

                        for i in updated_protocols:
                            if i['protocols_id'] == protocols_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['protocols_id'] == protocols_id for x in new_protocols):
                                new_protocols.append({'protocols_id': protocols_id})

                            for i in new_protocols:
                                if i['protocols_id'] == protocols_id:
                                    i[dictKey] = values
                elif (keys.split('.'))[0] == "isp":
                    updated_isp[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "supportive":
                    supportive_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['supportive_id'] ==  supportive_id for x in updated_supportive):
                            updated_supportive.append({'supportive_id': supportive_id})


                        for i in updated_supportive:
                            if i['supportive_id'] == supportive_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['supportive_id'] == supportive_id for x in new_supportive):
                                new_supportive.append({'supportive_id': supportive_id})

                            for i in new_supportive:
                                if i['supportive_id'] == supportive_id:
                                    i[dictKey] = values
                elif (keys.split('.'))[0] == "tracking":
                    tracking_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['tracking_id'] ==  tracking_id for x in updated_tracking):
                            updated_tracking.append({'tracking_id': tracking_id})

                        for i in updated_tracking:
                            if i['tracking_id'] == tracking_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['tracking_id'] == tracking_id for x in new_tracking):
                                new_tracking.append({'tracking_id': tracking_id})

                            for i in new_tracking:
                                if i['tracking_id'] == tracking_id:
                                    i[dictKey] = values
            print("updated_protocols:", updated_protocols)
            print("updated_isp:", updated_isp)
            print("updated_supportive:", updated_supportive)
            print("updated_tracking:", updated_tracking)

            requests.post(backendPOST + profile_id + '/isp', data=updated_isp)

            for i in updated_protocols:
                requests.post(backendPOST + profile_id + '/protocols', data=i)
            for i in new_protocols:
                i['patient_id'] = profile_id
                i.pop('protocols_id', None)
                print(i)
                requests.put(backendPOST + 'protocols/' + profile_id, data=i)


            for i in updated_supportive:
                requests.post(backendPOST + profile_id + '/supportive', data=i)
            for i in new_supportive:
                i['patient_id'] = profile_id
                i.pop('supportive_id', None)
                print(i)
                requests.put(backendPOST + 'supportive/' + profile_id, data=i)

            for i in updated_tracking:
                requests.post(backendPOST + profile_id + '/tracking', data=i)
            for i in new_tracking:
                i['patient_id'] = profile_id
                i.pop('tracking_id', None)
                print(i)
                requests.put(backendPOST + 'tracking/' + profile_id, data=i)
          

            return HttpResponseRedirect("/protocol/" + profile_id)
    elif page == "behavior":
        if request.method == "GET":
            return behavior(request, profile_id, True)
        else:
            print(request.POST)
            print('\n')
            updated_medical_treatment_plan = {}
            updated_behavior = {}
            updated_behavior_support_plans = {}
            #updated_restrictive = []
            #new_restrictive = []
            updated_rogers_monitor = {}

            for keys, values in request.POST.items():
                if (keys.split('.'))[0] == "medical_treatment_plan":
                    updated_medical_treatment_plan[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "behavior":
                    updated_behavior[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "behavior_support_plan":
                    updated_behavior_support_plans[keys.split('.')[1]] = values
                    '''elif (keys.split('.'))[0] == "restrictive":
                    restrictive_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['restrictive_id'] ==  restrictive_id for x in updated_restrictive):
                            updated_restrictive.append({'restrictive_id': restrictive_id})

                        for i in updated_restrictive:
                            if i['restrictive_id'] == restrictive_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['restrictive_id'] == restrictive_id for x in new_restrictive):
                                new_restrictive.append({'restrictive_id': restrictive_id})

                            for i in new_restrictive:
                                if i['restrictive_id'] == restrictive_id:
                                    i[dictKey] = values
                elif (keys.split('.'))[0] == "rogers_monitor":
                    updated_rogers_monitor[keys.split('.')[1]] = values '''

            print("updated_medical_treatment_plan:", updated_medical_treatment_plan)
            print("updated_behavior:", updated_behavior)
            print("updated_behavior_support_plans:", updated_behavior_support_plans)
            #print("updated_restrictive:", updated_restrictive)
            print("updated_rogers_monitor", updated_rogers_monitor)

            header = {'Content-Type': 'application/json'}
            updated_medical_treatment_plan = json.dumps({"updated_medical_treatment_plan" : updated_medical_treatment_plan})
            updated_behavior = json.dumps({"updated_behavior" : updated_behavior})
            updated_behavior_support_plans = json.dumps({"updated_behavior_support_plans" : updated_behavior_support_plans})
            #updated_restrictive = json.dumps({"updated_restrictive" : updated_restrictive})
            updated_rogers_monitor = json.dumps({"updated_rogers_monitor" : updated_rogers_monitor})


            requests.put(backendPOST + profile_id, data=updated_medical_treatment_plan, headers=header)
            requests.put(backendPOST + profile_id, data=updated_behavior, headers=header)
            requests.put(backendPOST + profile_id, data=updated_behavior_support_plans, headers=header)
            requests.put(backendPOST + profile_id, data=updated_rogers_monitor, headers=header)
            '''
            for i in updated_restrictive:
                requests.post(backendPOST + profile_id + '/restrictive', data=i)
            for i in new_restrictive:
                i['patient_id'] = profile_id
                i.pop('restrictive_id', None)
                print(i)
                requests.put(backendPOST + 'restrictive/' + profile_id, data=i) '''

            return HttpResponseRedirect("/behavior/" + profile_id)
    elif page == "support":
        if request.method == "GET":
            return support(request, profile_id, True)
        else:
            print(request.POST)
            print('\n')
            updated_legal_guardian = {}
            updated_insurance = []
            new_insurance = []
            updated_legal_status = []
            new_legal_status = []

            for keys, values in request.POST.items():

                if (keys.split('.'))[0] == "insurance":
                    insurance_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['insurance_id'] ==  insurance_id for x in updated_insurance):
                            updated_insurance.append({'insurance_id': insurance_id})

                        for i in updated_insurance:
                            if i['insurance_id'] == insurance_id:
                                i[dictKey] = values
                            else:
                                if values != '':
                                    if  not any(x['insurance_id'] == insurance_id for x in new_insurance):
                                        new_insurance.append({'insurance_id': insurance_id})

                                    for i in new_insurance:
                                        if i['insurance_id'] == insurance_id:
                                            i[dictKey] = values
                elif (keys.split('.'))[0] == "legal_guardian":
                    updated_legal_guardian[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "legal_status":
                    legal_status_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['legal_status_id'] ==  legal_status_id for x in updated_legal_status):
                            updated_legal_status.append({'legal_status_id': legal_status_id})

                        for i in updated_legal_status:
                            if i['legal_status_id'] == legal_status_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['legal_status_id'] == legal_status_id for x in new_legal_status):
                                new_legal_status.append({'legal_status_id': legal_status_id})

                            for i in new_legal_status:
                                if i['legal_status_id'] == legal_status_id:
                                    i[dictKey] = values

            print("updated_insurance:", updated_insurance)
            print("updated_legal_guardian:", updated_legal_guardian)
            print("updated_legal_status:", updated_legal_status)

            header = {'Content-Type': 'application/json'}
            updated_insurance = json.dumps({"updated_insurance" : updated_insurance})
            updated_legal_guardian = json.dumps({"updated_legal_guardian" : updated_legal_guardian})
            updated_legal_status = json.dumps({"updated_legal_status" : updated_legal_status})
            
            requests.post(backendPOST + profile_id, data=updated_insurance, headers=header)
            requests.post(backendPOST + profile_id, data=updated_legal_guardian, headers=header)
            requests.post(backendPOST + profile_id, data=updated_legal_status, headers=header)

            for i in updated_insurance:
                requests.post(backendPOST + profile_id + '/insurance', data=i)
            for i in new_insurance:
                i['patient_id'] = profile_id
                i.pop('insurance_id', None)
                print(i)
                requests.put(backendPOST + 'insurance/' + profile_id, data=i)
            for i in updated_legal_status:
                requests.post(backendPOST + profile_id + '/legal_status', data=i)
            for i in new_legal_status:
                i['patient_id'] = profile_id
                i.pop('legal_status_id', None)
                print(i)
                requests.put(backendPOST + 'legal_status' + profile_id, data=i)
            
            return HttpResponseRedirect("/support/" + profile_id)

def new(request):
    if request.method == "GET":
        return render(request, "new_profile.html")
    elif request.method == "POST":
        print(request.POST)
        print('\n')
        new_medical_info = {}
        new_basic_info = {}
        new_self_preservation = []
        new_identifying = {}
        new_legal_guardian = {}


        for keys, values in request.POST.items():
            if values != "":
                if (keys.split('.'))[0] == "basic_info":
                    new_basic_info[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "medical_info":
                    new_medical_info[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "identifying":
                    new_identifying[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "legal_guardian":
                    new_legal_guardian[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "self_preservation":
                    self_preservation_id = keys.split('.')[1]
                    dictKey = keys.split('.')[2]
                    # new entries to self_preservation
                    # check if theres even anything in them
                    if values != '':
                        # these are just edits to existing things
                        if not any(x['self_preservation_id'] == self_preservation_id for x in new_self_preservation):
                            new_self_preservation.append({'self_preservation_id': self_preservation_id})

                        for i in new_self_preservation:
                            if i['self_preservation_id'] == self_preservation_id:
                                i[dictKey] = values

        print("new_identifying:", new_identifying)
        print("new_medical_info:", new_medical_info)
        print("new_basic_info:", new_basic_info)
        print("new_self_prservation:", new_self_preservation)
        print("new_legal_guardian:", new_legal_guardian)

        # send all the new stuff
        #TODO: where do i get the resulting  id
        # do i do it before or after?
        response = requests.post(backendPOST[:-1],json={"name_first" : new_basic_info["name_first"],
                                        "name_last" : new_basic_info["name_last"]}).json()

        if new_identifying != {}:
            requests.put(backendPOST + 'identifying', data=new_identifying)
        if new_medical_info != {}:
            requests.put(backendPUT + 'medical_info', data=new_medical_info)
        if new_basic_info != {}:
            print(requests.put(backendPUT + 'basic', data=new_basic_info))
        if new_legal_guardian != {}:
            requests.put(backendPUT + 'legal_guardian', data=new_legal_guardian)
      
        for i in new_self_preservation:
            i.pop('self_preservation_id', None)
            print(i)
            requests.put(backendPUT + "/self_preservation/", data=i) 

        profile_id = str(response["id"]) or "1"

        return HttpResponseRedirect("/profile/" + profile_id)

def login(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return HttpResponseRedirect('/')
            else:
                print("Disabled Account")
                return render(request, 'signin.html', context={ 'error': 'Disabled Account'})
                # Return a 'disabled account' error message
                ...
        else:
            print("Invalid Login")
            return render(request, 'signin.html', context={})
            # Return an 'invalid login' error message.
            ...

def search(request):
    if request.method == 'POST':

        all_results = requests.get('http://127.0.0.1:5000/api/patient')
        all_results = all_results.json()

        for people in all_results['objects']:
            name_temp = people['name_first'] + ' ' + people['name_last']
            if request.POST['query'] == name_temp:
                return HttpResponseRedirect('/profile/' + str(people['id']))

    return render(request, "home-notFound.html")

def index(request):
    return render(request, "home.html")

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/signedout/")

def efs_gen(request, profile_id):
   output = PdfFileWriter()
   input = PdfFileReader(open("static/original.pdf", "rb"))

   #create response object
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename=EFS.pdf'

   result = requests.get(backendGET + profile_id)

   #get necessary JSON
   result = result.json()

   # generate watermark on the fly
   buffer = BytesIO() # create string buffer for PDF
   pdf = canvas.Canvas(buffer, pagesize=letter)
   fields = []
   fields.append((70, 755, result['name_first']))
   fields.append((140, 755, result['name_last']))
   fields.append((250, 755, result['basic_info']['name_preferred']))
   fields.append((120, 735, result['basic_info']['address_current']))
   fields.append((120, 715, result['basic_info']['address_former']))
   fields.append((40, 685, result['basic_info']['sex']))
   fields.append((70, 685, result['basic_info']['race']))
   fields.append((105, 685, result['basic_info']['birthday'][5:]))
   fields.append((155, 685, "30"))
   fields.append((185, 685, str(result['basic_info']['height'])))
   fields.append((225, 685, str(result['basic_info']['weight'])))
   fields.append((265, 685, result['basic_info']['build']))
   fields.append((305, 685, result['basic_info']['hair']))
   fields.append((342, 685, result['basic_info']['eyes']))
   fields.append((150, 670, result['basic_info']['distinguishing_marks']))
   fields.append((175, 650, result['basic_info']['competency_status']))
   fields.append((40, 620, result['legal_guardian']['guardian_name']))
   fields.append((225, 620, result['legal_guardian']['guardian_phone']))
   fields.append((40, 590, result['legal_guardian']['guardian_address']))
   fields.append((40, 560, result['legal_guardian']['family_address']))
   fields.append((225, 560, result['legal_guardian']['family_phone']))
   fields.append((40, 520, result['basic_info']['training_program_or_school_address']))
   fields.append((225, 520, result['basic_info']['training_program_or_school_phone']))
   fields.append((305, 520, result['basic_info']['work_address']))
   fields.append((510, 520, result['basic_info']['work_phone']))
   fields.append((40, 480, result['medical_info']['diagnoses']))
   fields.append((90, 465, result['medical_info']['allergies']))
   fields.append((40, 430, result['primary_physician']))
   fields.append((40, 405, result['basic_info']['primary_language']))
   fields.append((345, 405, result['identifying_info']['self_protection']))
   fields.append((40, 370, result['identifying_info']['behavior']))
   fields.append((345, 370, result['identifying_info']['response_to_search']))
   fields.append((40, 335, result['identifying_info']['movement_pattern']))
   fields.append((265, 335, result['identifying_info']['places_frequented']))
   fields.append((155, 205, result['contacts'][0]['name']))
   fields.append((427, 197, result['contacts'][0]['address']))


   for element in fields:
        if type(element[2]) == str:
            pdf.drawString(element[0],element[1],element[2])
   pdf.save()

   # put on watermark from buffer
   watermark = PdfFileReader(buffer)
   page1 = input.getPage(0)

   page1.mergePage(watermark.getPage(0))

   # add processed pdf page
   output.addPage(page1)

   #stream to browserxs
   outputStream = response
   output.write(response)
   outputStream.close()

   return response
