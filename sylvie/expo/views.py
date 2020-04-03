from django.shortcuts import render
from .models import ExpoModel

# Create your views here.

def renderExpo(request):
    expos = ExpoModel.objects.all()
    for expo in expos:
        print (expo.link)
    return(render(request, 'expo.html', {'expos':expos}))
