from django.shortcuts import render
from django.http import JsonResponse
from nutzserver.models import *
import json, requests
from django.core import serializers

backendGET = 'http://localhost:8000/backend/profile/'
backendPOST = 'http://localhost:8000/backend/profile/'

# Create your views here.
def backend(request, profile_id):
    if request.method == 'GET':
        profile = int(profile_id)
        if profile > 0:
            emfprofile = EMFProfile.objects.filter(id=profile)
        else:
            emfprofile = EMFProfile.objects.all()

        emfprofile = serializers.serialize('json', emfprofile)
        return JsonResponse(emfprofile, safe=False)
    elif request.method == 'POST':    
        pass


def get_request(request, profile_id, template):
	profile_data = requests.get(backendGET + profile_id)
	profile_data = json.loads(profile_data.json())

	return render(request, template, context={'basic_info': profile_data['basic_info'], 'legal_guardian': profile_data['legal_guardian'], 'medical': profile_data['medical'], 'identifying': profile_data['identifying'] })

def profile(request, profile_id):
    return get_request(request, profile_id, "profile.html")

def update(request, profile_id):
	if request.method == 'GET':
		return get_request(request, profile_id, "update.html")
	# elif request.method == 'POST'
	# 	requests.post(backendPOST + profile_id, data={'basic_info': request['basic_info'],
	# 										  'legal_guardian': profile_data['legal_guardian'],
	# 										  'medical': profile_data['medical'],
	# 										  'identifying': profile_data['identifying']} )
