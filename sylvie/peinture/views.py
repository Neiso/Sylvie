from django.shortcuts import render
from .models import Peinture

# Create your views here.

def renderStyle(request, style_name):
    peintures = Peinture.objects.filter(style=style_name)
    categories = []
    for peinture in peintures:
        if (peinture.categorie not in categories):
            categories.append(peinture.categorie)
    return render(request, "peinture.html", {'peintures':peintures, 'categories':categories})
