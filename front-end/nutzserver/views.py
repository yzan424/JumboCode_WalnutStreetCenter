from django.shortcuts import render
from django.http import JsonResponse
from nutzserver.models import *
import json
from django.core import serializers

# Create your views here.
def backend(request):
    if request.method == 'GET':
        profile = int(request.GET.get('profile'))
        if profile > 0:
            emfprofile = EMFProfile.objects.filter(id=profile)
        else:
            emfprofile = EMFProfile.objects.all()

        emfprofile = serializers.serialize('json', emfprofile)
        return JsonResponse(emfprofile, safe=False)
    elif request.method == 'POST':    
        pass
