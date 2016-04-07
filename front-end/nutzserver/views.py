from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from nutzserver.models import *
from django.template import *
import json, requests


backendGET = 'http://localhost:8000/backend/profile/'
backendPOST = 'http://localhost:8000/backend/profile/'
backendPUT = 'http://localhost:8000/backend/profile/'

# Create your views here.
def backend(request, profile_id, data):
    if request.method == 'GET':
        #create our response object
        if data == "basic":
            # this is the basic info, we return this under demographics
            # Here's how to access this info: http://localhost:8000/backend/profile/1/basic
            result = {
                "patient_id": profile_id,
                "state_id": "MA",
                "name_last": "Doe",
                "name_first": "John",
                "name_preferred": "JD",
                "birthday": "12/02/1994",
                "birthplace": "Somerville, MA",
                "social_security": "1231231234",
                "citizenship": "American",
                "phone": "1233333333",
                "phone_on_entry": "3213213333",
                "group_home": "14",
                "day_service": True,
                "training_program_or_school_address": "Tufts University",
                "training_program_or_school_phone": "23123123123",
                "area_office": "That office over yonder",
                "record_location": "Here",
                "address_current": "5th Avenue, New York, NY",
                "address_former": "6th Ave. New York, NY",
                "sex": "Male",
                "race": "White",
                "blood_type": "AB",
                "religion": "Atheist",
                "marital_status": "single",
                "primary_language": "English",
                "height": 173,
                "weight": 155.5,
                "build": "Jacked",
                "hair": "Hazelnut Brown",
                "eyes": "Gorgeous",
                "distinguishing_marks": "None",
                "competency_status": "pretty competent",
                "eligitbility_date": "1/1/2017",
                "area_meaningful_tie": "Mom",
                "referral_source": "John McDoe",
                "accompanied_by": "Mom",
                "work_phone": "1231231234",
                "work_address": "5th Avenue, New York, NY"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "legal_guardian":
            # Access: http://localhost:8000/backend/profile/1/legal_guardian
            result = {
                "patient_id": profile_id,
                "guardian_name": "John Cena",
                "guardian_phone": "1233334323",
                "guardian_address": "7th Avenue New York, NY",
                "father_name": "John Doe Sr.",
                "father_birthday": "1/1/2018",
                "father_birthplace": "Kansas",
                "father_alive": True,
                "mother_maiden_name": "Maiden",
                "mother_birthday": "1/17/2014",
                "mother_birthplace": "Washington DC",
                "mother_alive": True,
                "parents_marital_status": "Married",
                "family_phone": "4177777777",
                "family_address": "16th Ave., New York, NY"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "medical":
            # Access: http://localhost:8000/backend/profile/1/medical
            result = {
                "patient_id": profile_id,
                "physician_id": 17,
                "diagnoses": "Flu",
                "allergies": "Pollen",
                "alzheimers_dementia": False,
                "down_syndrome": False,
                "vision_problem": False
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "identifying":
            # Access: http://localhost:8000/backend/profile/1/identifying
            result = {
                "patient_id": profile_id,
                "self_protection": "Knows martial arts",
                "behavior": "Very Chill",
                "response_to_search": "Yes",
                "movement_pattern": "Only walks in circles",
                "places_frequented": "McDonalds",
                "travel_method": "By flying on broomsticks",
                "carries_ID": True,
                "surrounding_awareness": "He's aware of what's going on",
                "last_update": "1/1/2014"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "self_preservation":
            # Access: http://localhost:8000/backend/profile/1/self_preservation
            result = [{
                "patient_id": profile_id,
                "self_preservation_id": 18,
                "assessment": "He cares for himself",
                "cause_of_failure": "Too much fun",
                "determination_basis": "random",
                "date_occured": "1/1/2015"
            },{
                "patient_id": profile_id,
                "self_preservation_id": 11,
                "assessment": "He cares for himself lol",
                "cause_of_failure": "Too much sass",
                "determination_basis": "randomly",
                "date_occured": "1/1/2014"
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "insurance":
            # Access: http://localhost:8000/backend/profile/1/insurance
            result = [{
                "patient_id": profile_id,
                "health_insurance_and_other_id": "123123123123123",
                "source": "Health Insurance Co.",
                "type_of": "Full coverage",
                "id_number": "812381238123",
                "benefits": "Free wifi everywhere",
                "expiration_date": "1/1/2017",
                "expired": False
            },{
                "patient_id": profile_id,
                "health_insurance_and_other_id": "1111",
                "source": "Tufts insurance.",
                "type_of": "Full coverage",
                "id_number": "494949494",
                "benefits": "Unlimited wifi everywhere",
                "expiration_date": "1/1/2017",
                "expired": False
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "legal_competency":
            # Access: http://localhost:8000/backend/profile/1/legal_competency
            result = [{
                "patient_id": profile_id,
                "legal_competency_id": 17,
                "status": "Independent",
                "type_of": "Legal Status",
                "adjudiction_date": "5/1/2015",
                "requested_by": "Steven McDoe",
                "date_requested": "1/17/2014"
            },{
                "patient_id": profile_id,
                "legal_competency_id": 18,
                "status": "Medicare",
                "type_of": "Legal Status 2",
                "adjudiction_date": "5/1/2014",
                "requested_by": "Steven John",
                "date_requested": "1/17/2015"
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "service_providers":
            # Access: http://localhost:8000/backend/profile/1/service_providers
            result = [{
                "patient_id": profile_id,
                "service_providers_id": 15,
                "start_date": "1/1/2015",
                "stop_date": "12/31/2015",

            }, {
                "patient_id": profile_id,
                "service_providers_id": 15,
                "start_date": "1/1/2015",
                "stop_date": "12/31/2015",

            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "protocols":
            # Access: http://localhost:8000/backend/profile/1/protocols
            result = [{
                "protocol_id": 2,
                "patient_id": profile_id,
                "name": "Transport",
                "description": "When traveling to an airport",
                "appointment_id": 47,
                "guardian_signature_date": "1/1/2011",
                "physician_signature_date": "2/2/2012"

            }, {
                "protocol_id": 2,
                "patient_id": profile_id,
                "name": "Transport",
                "description": "When traveling to an airport",
                "appointment_id": 47,
                "guardian_signature_date": "1/1/2011",
                "physician_signature_date": "2/2/2012"
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "supportive":
            # Access: http://localhost:8000/backend/profile/1/supportive
            result = [{
                "supportive_protective_devices_id": 17,
                "patient_id": profile_id,
                "device_type": "Listening Aid",
                "hrc_approval_date": "1/1/2012",
                "hrc_submission_date": "2/3/2014",
                "physician_signature": True,
                "nurse_signature": False
            },{
                "supportive_protective_devices_id": 18,
                "patient_id": profile_id,
                "device_type": "Listening Aid 2",
                "hrc_approval_date": "1/1/2012",
                "hrc_submission_date": "2/3/2014",
                "physician_signature": True,
                "nurse_signature": False
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "isp":
            # Access: http://localhost:8000/backend/profile/1/isp
            result = {
                "individual_support_plan_id": 17,
                "patient_id": profile_id,
                "last_isp_date": "1/1/2012",
                "comments": ""
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "tracking":
            # Access: http://localhost:8000/backend/profile/1/tracking
            result = [{
                "tracking_id": 12,
                "tracking_name": "GPS",
                "description": "This is a tracking GPS",
                "patient_id": profile_id,
                "most_recent": "1/1/2012",
                "next_due": 12
            }, {
                "tracking_id": 13,
                "tracking_name": "GPS2",
                "description": "This is a tracking GPS2",
                "patient_id": profile_id,
                "most_recent": "1/1/2012",
                "next_due": 12
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "medical_treatment_plan":
            # Access: http://localhost:8000/backend/profile/1/medical_treatment_plan
            result = {
                "medical_treatment_plan_id": 12,
                "patient_id": profile_id,
                "guardian_signature_date": "1/1/2012",
                "appointment_id": 12,
                "medications": "Drugs",
                "diagnoses": "sick",
                "symptoms": "not feeling well"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "behavior":
            # Access: http://localhost:8000/backend/profile/1/behavior
            result = {
                "patient_id": profile_id,
                "assessment_date": "1/1/2012",
                "behavior": "not chill",
                "summary": "Be chill"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "restrictive":
            # Access: http://localhost:8000/backend/profile/1/restrictive
            result = [{
                "patient_id": profile_id,
                "restrictive_practices_id": 15,
                "practice_type": "Door Lock",
                "hrc_approval_date": "1/3/2015",
                "hrc_submission_date": "12/2/2014",
                "description": "we lock the doors on the front"
            },
            {
                "patient_id": profile_id,
                "restrictive_practices_id": 16,
                "practice_type": "Door Lock 2",
                "hrc_approval_date": "1/3/2015",
                "hrc_submission_date": "12/2/2014",
                "description": "we lock the doors on the front"
            }]
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "behavior_support_plans":
            # Access: http://localhost:8000/backend/profile/1/behavior_support_plans
            result = {
                "patient_id": profile_id,
                "guardian_signature_date": "1/1/2013",
                "residential_appointment_id": 15,
                "day_appointment_id": 12,
                "tier": "third"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif data == "rogers_monitor":
            # Access: http://localhost:8000/backend/profile/1/rogers_monitor
            result = {
                "patient_id": profile_id,
                "next_court_date": "1/1/2012",
                "last_court_date": "10/2/2014",
                "guardian_signature_date": "1/1/2012",
                "appointment_id": 1,
                "medications": "None"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
    else:
        # TODO: Probably should return something else    
        return JsonResponse({"success": True})

def profile(request, profile_id, edit):
    medical_info = requests.get(backendGET + profile_id + '/medical/')
    basic_info = requests.get(backendGET + profile_id + '/basic/')
    self_preservation = requests.get(backendGET + profile_id + '/self_preservation/')
    identifying = requests.get(backendGET + profile_id + '/identifying/') 
    legal_guardian = requests.get(backendGET + profile_id + '/legal_guardian/') 

    medical_info = json.loads(medical_info.json())
    basic_info = json.loads(basic_info.json())
    self_preservation = json.loads(self_preservation.json())
    identifying = json.loads(identifying.json())
    legal_guardian = json.loads(legal_guardian.json())
        
    if edit == False:
        return render(request, "profile.html", context={'medical_info': medical_info, 'basic_info': basic_info, 'self_preservation': self_preservation, 'identifying': identifying, "legal_guardian": legal_guardian})
    else:
        return render(request, "update_profile.html", context={'medical_info': medical_info, 'basic_info': basic_info, 'self_preservation': self_preservation, 'identifying': identifying, "legal_guardian": legal_guardian})        

def protocol(request, profile_id, edit):
    protocols = requests.get(backendGET + profile_id + '/protocols/')
    isp = requests.get(backendGET + profile_id + '/isp')
    supportive = requests.get(backendGET + profile_id + '/supportive/')
    tracking = requests.get(backendGET + profile_id + '/tracking/')  

    protocols = json.loads(protocols.json())
    isp = json.loads(isp.json())
    supportive = json.loads(supportive.json())
    tracking = json.loads(tracking.json())

    if edit == False:
        return render(request, "protocol.html", context={'protocols': protocols, 'isp': isp, 'supportive': supportive, 'tracking': tracking})
    else:
        return render(request, "update_protocol.html", context={'protocols': protocols, 'isp': isp, 'supportive': supportive, 'tracking': tracking})        

def behavior(request, profile_id, edit):
    medical_treatment_plan = requests.get(backendGET + profile_id + '/medical_treatment_plan/')
    behavior = requests.get(backendGET + profile_id + '/behavior/')
    behavior_support_plans = requests.get(backendGET + profile_id + '/behavior_support_plans/')
    restrictive = requests.get(backendGET + profile_id + '/restrictive/')
    rogers_monitor = requests.get(backendGET + profile_id + '/rogers_monitor/')

    medical_treatment_plan = json.loads(medical_treatment_plan.json())
    behavior = json.loads(behavior.json())
    behavior_support_plans = json.loads(behavior_support_plans.json())
    restrictive = json.loads(restrictive.json())
    rogers_monitor = json.loads(rogers_monitor.json())
        
    if edit == False:
        return render(request, "behavior.html", context={'medical_treatment_plan': medical_treatment_plan, 'behavior': behavior, 'behavior_support_plans': behavior_support_plans, 'restrictive': restrictive, 'rogers_monitor': rogers_monitor})
    else:
        return render(request, "update_behavior.html", context={'medical_treatment_plan': medical_treatment_plan, 'behavior': behavior, 'behavior_support_plans': behavior_support_plans, 'restrictive': restrictive, 'rogers_monitor': rogers_monitor})        


def support(request, profile_id, edit):
    legal_guardian = requests.get(backendGET + profile_id + '/legal_guardian/')
    insurance = requests.get(backendGET + profile_id + '/insurance/')
    legal_status = requests.get(backendGET + profile_id + '/legal_competency/')

    legal_guardian = json.loads(legal_guardian.json())
    insurance = json.loads(insurance.json())
    legal_status = json.loads(legal_status.json())
        
    if edit == False:
        return render(request, "support.html", context={'legal_guardian': legal_guardian, 'insurance': insurance, 'legal_status': legal_status})
    else:
        return render(request, "update_support.html", context={'legal_guardian': legal_guardian, 'insurance': insurance, 'legal_status': legal_status})        

def edit(request, page, profile_id):
    if page == 'profile':
        if request.method == 'GET':
            return profile(request, profile_id, True)
        else:
            # send the new stuffs to the backend
            print(request.POST)
            print('\n')
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
                    self_preservation_id = keys.split('.')[2]
                    dictKey = keys.split('.')[3]
                    if (keys.split('.')[1] == "existing"):
                        # these are just edits to existing things
                        # create a new dictionary if it does not exist
                        if not any(x['self_preservation_id'] == self_preservation_id for x in updated_self_preservation):
                            updated_self_preservation.append({'self_preservation_id': self_preservation_id})

                        for i in updated_self_preservation:
                            if i['self_preservation_id'] == self_preservation_id:
                                i[dictKey] = values
                    else:
                        # new entries to self_preservation
                        # check if theres even anything in them
                        if values != '':
                            # these are just edits to existing things
                            if not any(x['self_preservation_id'] == self_preservation_id for x in new_self_preservation):
                                new_self_preservation.append({'self_preservation_id': self_preservation_id})

                            for i in new_self_preservation:
                                if i['self_preservation_id'] == self_preservation_id:
                                    i[dictKey] = values

            print("updated_identifying:", updated_identifying)
            print("updated_medical_info:", updated_medical_info)
            print("updated_basic_info:", updated_basic_info)
            print("updated_self_prservation:", updated_self_preservation)
            print("new_self_preservation:", new_self_preservation)
            print("updated_legal_guardian:", updated_legal_guardian)

            # send all the new stuff
            requests.post(backendPOST + profile_id + '/identifying/', data=updated_identifying)
            requests.post(backendPOST + profile_id + '/medical_info/', data=updated_medical_info)
            requests.post(backendPOST + profile_id + '/basic/', data=updated_basic_info)
            requests.post(backendPOST + profile_id + '/legal_guardian/', data=updated_legal_guardian)
            for i in updated_self_preservation:
                requests.post(backendPOST + profile_id + '/self_preservation/', data=i)           
            for i in new_self_preservation:
                i.pop('self_preservation_id', None)
                print(i)
                requests.put(backendPOST + "/self_preservation/", data=i) 

            return HttpResponseRedirect("/profile/" + profile_id + '/')
    elif page == "protocol":
        if request.method == "GET":
            return protocol(request, profile_id, True)
        else:
            # send new info
            pass
            #redirect
    elif page == "behavior":
        if request.method == "GET":
            return behavior(request, profile_id, True)
        else:
            pass
    elif page == "support":
        if request.method == "GET":
            return support(request, profile_id, True)
        else:
            pass


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
                login(request, user)
            # Redirect to a success page.
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


