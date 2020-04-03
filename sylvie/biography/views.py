from django.shortcuts import render
from expo.models import ExpoModel
import datetime

# Create your views here.

def renderBiography(request):
    today = datetime.datetime.now().date()
    expos = ExpoModel.objects.order_by('date')
    expo_liste = []
    for expo in expos :
        if (today <= expo.date):
            expo_liste.append(expo)
        if (len(expo_liste) == 3):
            break
    for expo in expo_liste:
        if len(expo.desc) > 85:
            expo.desc = expo.desc[0:97] + "..."
    return render(request, "biography.html", {'expos':expo_liste})