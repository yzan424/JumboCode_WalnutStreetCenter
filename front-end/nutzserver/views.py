from django.shortcuts import render
from django.http import JsonResponse
from nutzserver.models import *
import json, requests


backendGET = 'http://localhost:8000/backend/profile/'
backendPOST = 'http://localhost:8000/backend/profile/'

# Create your views here.
def backend(request, profile_id):
    if request.method == 'GET':
        #create our response object
        emfprofile = {}
        emfprofile['id'] = int(profile_id)
        emfprofile['status_code'] = 200

        emfprofile['basic_info'] = {}
        emfprofile['basic_info']['patient_id'] = 1
        emfprofile['basic_info']['state_id'] = 1
        emfprofile['basic_info']['name_last'] = "Doe"
        emfprofile['basic_info']['name_first'] = "John"
        emfprofile['basic_info']['name_preferred'] = "JD"
        emfprofile['basic_info']['birthday'] = "12/02/1994"
        emfprofile['basic_info']['birthplace'] = "Manila, Philippines"
        emfprofile['basic_info']['social_security'] = 1233211234
        emfprofile['basic_info']['citizenship'] = "Murica"
        emfprofile['basic_info']['phone'] = 12332112313
        emfprofile['basic_info']['phone_on_entry'] = 1234578910
        emfprofile['basic_info']['group_home'] = "Our Group Home"
        emfprofile['basic_info']['day_service'] = True
        emfprofile['basic_info']['training_program_or_school_address'] = "1234 Address Road"
        emfprofile['basic_info']['training_program_or_school_phone'] = 1231231231
        emfprofile['basic_info']['area_office'] = "THE AREA OFFICE!"
        emfprofile['basic_info']['record_location'] = "This is the record location"
        emfprofile['basic_info']['address_current'] = "1234 Current Address Road, MA"
        emfprofile['basic_info']['address_former'] = "1234 Former Address Lane"
        emfprofile['basic_info']['sex'] = "Male"
        emfprofile['basic_info']['race'] = "1234 Address Road"
        emfprofile['basic_info']['blood_type'] = "AB+"
        emfprofile['basic_info']['religion'] = "Judaism"
        emfprofile['basic_info']['marital_status'] = "Single"
        emfprofile['basic_info']['primary_language'] = "English"
        emfprofile['basic_info']['height'] = "180"
        emfprofile['basic_info']['weight'] = "170"
        emfprofile['basic_info']['build'] = "Jacked"
        emfprofile['basic_info']['hair'] = "black"
        emfprofile['basic_info']['eyes'] = "brown"
        emfprofile['basic_info']['distinguishing marks'] = "Judaism"
        emfprofile['basic_info']['competency_status'] = "Competent"
        emfprofile['basic_info']['eligibility_date'] = "12/02/1994"
        emfprofile['basic_info']['area_meaningful_tie'] = "This is a meaningful tie"
        emfprofile['basic_info']['referral_source'] = "Mom"
        emfprofile['basic_info']['accompanied_by'] = "Dad"
        emfprofile['basic_info']['work_phone'] = 1231231231
        emfprofile['basic_info']['work_address'] = "1234 Work Address Road"

        emfprofile['legal_guardian'] = {}
        emfprofile['legal_guardian']['guardian_name'] = "Guardian McGee"
        emfprofile['legal_guardian']['guardian_phone'] = 123123123123
        emfprofile['legal_guardian']['guardian_address'] = "1234 GuardAddress Rd."
        emfprofile['legal_guardian']['father_name'] = "Daddy McGee"
        emfprofile['legal_guardian']['father_birthday'] = "12/02/1994"
        emfprofile['legal_guardian']['father_birthplace'] = "Compton, CA"
        emfprofile['legal_guardian']['father_alive'] = True
        emfprofile['legal_guardian']['mother_maiden_name'] = "Dorian"
        emfprofile['legal_guardian']['mother_birthday'] = "12/02/1994"
        emfprofile['legal_guardian']['mother_birthplace'] = "New York, NY"
        emfprofile['legal_guardian']['mother_alive'] = True
        emfprofile['legal_guardian']['parents_marital_status'] = True
        emfprofile['legal_guardian']['family_phone'] = 1231231233
        emfprofile['legal_guardian']['family_address'] = "1234 Family Address Lane"

        emfprofile['medical'] = {}
        emfprofile['medical']['physician_id'] = 1
        emfprofile['medical']['diagnoses'] = "I'm a disease"
        emfprofile['medical']['allergies'] = "Walnutz"
        emfprofile['medical']['alzheimers_dementia'] = False
        emfprofile['medical']['down_syndrome'] = False
        emfprofile['medical']['vision_problem'] = True

        emfprofile['identifying'] = {}
        emfprofile['identifying']['self_protection'] = "YES, knows martial arts"
        emfprofile['identifying']['behavior'] = "Drinks coffee"
        emfprofile['identifying']['response_to_search'] = "yes"
        emfprofile['identifying']['movement_pattern'] = "Figure 8's"
        emfprofile['identifying']['places_frequented'] = "Starbucks"
        emfprofile['identifying']['travel_method'] = "Jetpack"
        emfprofile['identifying']['carries_ID'] = True
        emfprofile['identifying']['surrounding_awareness'] = "Knows what's going on"

        emfprofile = json.dumps(emfprofile)
        return JsonResponse(emfprofile, safe=False)
    elif request.method == 'POST':    
        return JsonResponse({"success": True})


def get_request(request, profile_id, template):
    profile_data = requests.get(backendGET + profile_id + '/')
    profile_data = json.loads(profile_data.json())

    return render(request, template, context={'basic_info': profile_data['basic_info'], 'legal_guardian': profile_data['legal_guardian'], 'medical': profile_data['medical'], 'identifying': profile_data['identifying']})

def profile(request, profile_id):
    return get_request(request, profile_id, "profile.html")

def update(request, profile_id):
    if request.method == 'GET':
        return get_request(request, profile_id, "update.html")
    elif request.method == 'POST':
        requests.post(backendPOST + profile_id, data={'basic_info': request['basic_info'],
                                              'legal_guardian': profile_data['legal_guardian'],
                                              'medical': profile_data['medical'],
                                              'identifying': profile_data['identifying']} )

