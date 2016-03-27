from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from nutzserver.models import *
from django.template import *
import json, requests


backendGET = 'http://localhost:8000/backend/profile/'
backendPOST = 'http://localhost:8000/backend/profile/'

# Create your views here.
def backend(request, profile_id):
    if request.method == 'GET':
        #create our response object
        if request.GET['data'] == "basic":
            # this is the basic info, we return this under demographics
            # Here's how to access this info: http://localhost:8000/backend/profile/1?data=basic
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
        elif request.GET['data'] == "legal_guardian":
            # Access: http://localhost:8000/backend/profile/1?data=legal_guardian
            result = {
                "patient_id": profile_id,
                "guardian_name": "John Cena",
                "guardian_phone": "1233334323",
                "guardian_address": "7th Avenue New York, NY",
                "father_name": "John Doe Sr.",
                "father_birthday": "1/1/2018",
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
        elif request.GET['data'] == "medical":
            # Access: http://localhost:8000/backend/profile/1?data=medical
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
        elif request.GET['data'] == "identifying":
            # Access: http://localhost:8000/backend/profile/1?data=identifying
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
        elif request.GET['data'] == "self_preservation":
            # Access: http://localhost:8000/backend/profile/1?data=self_preservation
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
        elif request.GET['data'] == "insurance":
            # Access: http://localhost:8000/backend/profile/1?data=insurance
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
        elif request.GET['data'] == "legal_competency":
            # Access: http://localhost:8000/backend/profile/1?data=legal_competency
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
        elif request.GET['data'] == "service_providers":
            # Access: http://localhost:8000/backend/profile/1?data=service_providers
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
        elif request.GET['data'] == "protocols":
            # Access: http://localhost:8000/backend/profile/1?data=protocols
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
        elif request.GET['data'] == "supportive":
            # Access: http://localhost:8000/backend/profile/1?data=supportive
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
        elif request.GET['data'] == "isp":
            # Access: http://localhost:8000/backend/profile/1?data=isp
            result = {
                "individual_support_plan_id": 17,
                "patient_id": profile_id,
                "last_isp_date": "1/1/2012",
                "Comments": ""
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif request.GET['data'] == "tracking":
            # Access: http://localhost:8000/backend/profile/1?data=tracking
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
        elif request.GET['data'] == "medical_treatment_plan":
            # Access: http://localhost:8000/backend/profile/1?data=medical_treatment_plan
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
        elif request.GET['data'] == "behavior":
            # Access: http://localhost:8000/backend/profile/1?data=behavior
            result = {
                "patient_id": profile_id,
                "assessment_date": "1/1/2012",
                "behavior": "not chill",
                "summary": "Be chill"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif request.GET['data'] == "restrictive":
            # Access: http://localhost:8000/backend/profile/1?data=restrictive
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
        elif request.GET['data'] == "behavior_support_plans":
            # Access: http://localhost:8000/backend/profile/1?data=behavior_support_plans
            result = {
                "patient_id": profile_id,
                "guardian_signature_date": "1/1/2013",
                "residential_appointment_id": 15,
                "day_appointment_id": 12,
                "tier": "third"
            }
            result = json.dumps(result)
            return JsonResponse(result, safe=False)
        elif request.GET['data'] == "rogers_monitor":
            # Access: http://localhost:8000/backend/profile/1?data=rogers_monitor
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
    elif request.method == 'POST':
        # TODO: Probably should return something else    
        return JsonResponse({"success": True})


def get_request(request, profile_id, template):
    profile_data = requests.get(backendGET + profile_id + '/')
    profile_data = json.loads(profile_data.json())

    return render(request, template, context={'id': profile_id, 'basic_info': profile_data['basic_info'], 'legal_guardian': profile_data['legal_guardian'], 'medical': profile_data['medical'], 'identifying': profile_data['identifying']})

def profile(request, profile_id):
    return get_request(request, profile_id, "profile.html")

def update(request, profile_id):
    if request.method == 'GET':
        return get_request(request, profile_id, "update.html")
    elif request.method == 'POST':


        emfprofile = {}
        emfprofile['id'] = profile_id
        emfprofile['basic_info'] = {}
        emfprofile['legal_guardian'] = {}
        emfprofile['medical'] = {}
        emfprofile['identifying'] = {}

        for elems in request.POST:
                if elems != 'csrfmiddlewaretoken':
                        category, key = elems.split('_', 1)
                if category == 'basic':
                        emfprofile['basic_info'][key] = request.POST[elems]
                elif category == 'legal':
                        emfprofile['legal_guardian'][key] = request.POST[elems]
                elif category == 'medical':
                        emfprofile['medical'][key] = request.POST[elems]
                elif category == 'identifying':
                        emfprofile['identifying'][key] = request.POST[elems]
                else:
                        print("We dun fucked up")




        requests.post(backendPOST + profile_id + '/', data=emfprofile )

        #in production redirect to the profile page
        return JsonResponse(json.dumps(emfprofile), safe=False)



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
