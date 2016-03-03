from django.shortcuts import render
from django.http import JsonResponse
from nutzserver.models import *
import json, requests
from django.core import serializers

backendGET = 'http://localhost:8000/backend/profile/'

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

def profile(request):
    profile_data = requests.get(backendGET + '0') #make a request to the backend
    profile_data = json.loads(profile_data.json()) # parse response 
    profile_fields = profile_data[0]['fields']

    print(profile_fields)

    for x in profile_data[0]['fields']:
        print(x)
        print(profile_data[0]['fields'][x])

    return render(request, "profile.html", context={'profile_fields': profile_fields})