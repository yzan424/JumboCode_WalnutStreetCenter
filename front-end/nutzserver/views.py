from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from nutzserver.models import *
from django.template import *
import json, requests


backendGET = 'http://52.88.243.201:5000/api/patient/'
backendPOST = 'http://52.88.243.201:5000/api/patient/'
backendPUT = 'http://52.88.243.201:5000/api/patient/'

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
                    dictKey = keys.split('.')[2]
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
                    dictKey = keys.split('.')[2]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['supportive_id'] ==  supportive_id for x in updated_supportive):
                            updated_supportive.append({'supportive_id': supportive_id})

                        for i in updated_supportive:
                            if i['supportive_id'] == supportive_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['supportive_id'] == supportive_id for x in new_supportive):
                                new_supportive.apped({'supportive_id': supportive_id})

                            for i in new_supportive:
                                if i['supportive_id'] == supportive_id:
                                    i[dictKey] = values
                elif (keys.split('.'))[0] == "tracking":
                    tracking_id = keys.split('.')[2]
                    dictKey = keys.split('.')[2]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['tracking_id'] ==  tracking_id for x in updated_tracking):
                            updated_tracking.append({'tracking_id': tracking_id})

                        for i in updated_tracking:
                            if i['tracking_id'] == tracking_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['tracking_id'] == tracking_id for x in new_tracking):
                                new_tracking.apped({'tracking_id': tracking_id})

                            for i in new_tracking:
                                if i['tracking_id'] == tracking_id:
                                    i[dictKey] = values
            print("updated_protocols:", updated_protocols)
            print("updated_isp:", updated_isp)
            print("updated_supportive:", updated_supportive)
            print("updated_tracking:", updated_tracking)

            requests.post(backendPOST + profile_id + '/protocols/', data=updated_protocols)
            requests.post(backendPOST + profile_id + '/isp/', data=updated_isp)
            requests.post(backendPOST + profile_id + '/supportive/', data=updated_supportive)
            requests.post(backendPOST + profile_id + '/tracking/', data=updated_tracking)

            for i in updated_protocols:
                requests.post(backendPOST + profile_id + '/protocols/', data=i)
            for i in new_protocols:
                i['patient_id'] = profile_id
                i.pop('protocols_id', None)
                print(i)
                requests.put(backendPOST + 'protocols/' + profile_id, data=i)

            for i in updated_supportive:
                requests.post(backendPOST + profile_id + '/supportive/', data=i)
            for i in new_supportive:
                i['patient_id'] = profile_id
                i.pop('supportive_id', None)
                print(i)
                requests.put(backendPOST + 'supportive/' + profile_id, data=i)

            for i in updated_tracking:
                requests.post(backendPOST + profile_id + '/tracking/', data=i)
            for i in new_tracking:
                i['patient_id'] = profile_id
                i.pop('tracking_id', None)
                print(i)
                requests.put(backendPOST + 'tracking/' + profile_id, data=i)
            #I'm not sure if i need to mimic the above block for every array in this set

            return HttpResponseRedirect("/protocol/" + profile_id + '/')
    elif page == "behavior":
        if request.method == "GET":
            return behavior(request, profile_id, True)
        else:
            print(request.POST)
            print('\n')
            updated_medical_treatment_plan = {}
            updated_behavior = {}
            updated_behavior_support_plans = {}
            updated_restrictive = []
            new_restrictive = []
            updated_rogers_monitor = {}

            for keys, values in request.POST.items():
                if (keys.split('.'))[0] == "medical_treatment_plan":
                    updated_medical_treatment_plan[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "behavior":
                    updated_behavior[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "behavior_support_plans":
                    updated_behavior_support_plans[keys.split('.')[1]] = values
                elif (keys.split('.'))[0] == "updated_restrictive":
                    restrictive_id = keys.split('.')[2]
                    dictKey = keys.split('.')[2]
                    if (keys.split('.')[1] == "existing"):
                        if not any(x['restrictive_id'] ==  restrictive_id for x in updated_restrictive):
                            updated_restrictive.append({'restrictive_id': restrictive_id})

                        for i in updated_restrictive:
                            if i['restrictive_id'] == restrictive_id:
                                i[dictKey] = values
                    else:
                        if values != '':
                            if  not any(x['restrictive_id'] == restrictive_id for x in new_restrictive):
                                new_restrictive.apped({'restrictive_id': restrictive_id})

                            for i in new_restrictive:
                                if i['restrictive_id'] == restrictive_id:
                                    i[dictKey] = values
                elif (keys.split('.'))[0] == "updated_rogers_monitor":
                    updated_rogers_monitor[keys.split('.')[1]] = values
            print("updated_medical_treatment_plan:", updated_medical_treatment_plan)
            print("updated_behavior:", updated_behavior)
            print("updated_behavior_support_plans:", updated_behavior_support_plans)
            print("updated_restrictive:", updated_restrictive)
            print("updated_rogers_monitor", updated_rogers_monitor)

            requests.post(backendPOST + profile_id + '/medical_treatment_plan/', data=updated_medical_treatment_plan)
            requests.post(backendPOST + profile_id + '/behavior/', data=updated_behavior)
            requests.post(backendPOST + profile_id + '/behavior_support_plans/', data=updated_behavior_support_plans)
            requests.post(backendPOST + profile_id + '/rogers_monitor/', data=updated_rogers_monitor)

            for i in updated_restrictive:
                requests.post(backendPOST + profile_id + '/restrictive/', data=i)
            for i in new_restrictive:
                i['patient_id'] = profile_id
                i.pop('restrictive_id', None)
                print(i)
                requests.put(backendPOST + 'restrictive/' + profile_id, data=i)

            return HttpResponseRedirect("/behavior/" + profile_id + '/')

    elif page == "support":
        if request.method == "GET":
            return support(request, profile_id, True)
        else:
            print(get.POST)
            print('\n')
            updated_legal_guardian = {}
            updated_insurance = []
            new_insurance = []
            updated_legal_status = []
            new_legal_status = []

            for keys, values in request.POST.items():

                if (keys.split('.'))[0] == "insurance":
                    insurance_id = keys.split('.')[2]
                    dictKey = keys.split('.')[2]
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
                        dictKey = keys.split('.')[2]
                        if (keys.split('.')[1] == "existing"):
                            if not any(x['legal_status_id'] ==  legal_status_id for x in updated_legal_status):
                                updated_legal_status.append({'legal_status_id': legal_status_id})

                            for i in updated_legal_status:
                                if i['legal_status_id'] == legal_status_id:
                                    i[dictKey] = values
                        else:
                            if values != '':
                                if  not any(x['legal_status_id'] == legal_status_id for x in new_legal_status):
                                    new_legal_status.apped({'legal_status_id': legal_status_id})

                                for i in new_legal_status:
                                    if i['legal_status_id'] == legal_status_id:
                                        i[dictKey] = values

            print("updated_insurance:", updated_insurance)
            print("updated_legal_guardian:", legal_guardian)
            print("updated_legal_status:", updated_legal_status)

            requests.post(backendPOST + profile_id + '/insurance/', data=updated_insurance)
            requests.post(backendPOST + profile_id + '/legal_guardian/', data=updated_legal_guardian)
            requests.post(backendPOST + profile_id + '/legal_status/', data=updated_legal_status)

            for i in updated_insurance:
                requests.post(backendPOST + profile_id + '/insurance/', data=i)
            for i in new_insurance:
                i['patient_id'] = profile_id
                i.pop('insurance_id', None)
                print(i)
                requests.put(backendPOST + 'insurance/' + profile_id, data=i)
            for i in updated_legal_status:
                requests.post(backendPOST + profile_id + '/legal_status/', data=i)
            for i in new_legal_status:
                i['patient_id'] = profile_id
                i.pop('legal_status_id', None)
                print(i)
                requests.put(backendPOST + 'legal_status/' + profile_id, data=i)
            
            return HttpResponseRedirect("/support/" + profile_id + '/')

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
        if new_identifying != {}:
            requests.put(backendPUT + 'identifying/', data=new_identifying)
        if new_medical_info != {}:
            requests.put(backendPUT + 'medical_info/', data=new_medical_info)
        if new_basic_info != {}:
            requests.put(backendPUT + 'basic/', data=new_basic_info)
        if new_legal_guardian != {}:
            requests.put(backendPUT + 'legal_guardian/', data=new_legal_guardian)
      
        for i in new_self_preservation:
            i.pop('self_preservation_id', None)
            print(i)
            requests.put(backendPUT + "/self_preservation/", data=i) 

        profile_id = "1"

        return HttpResponseRedirect("/profile/" + profile_id + '/')

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


