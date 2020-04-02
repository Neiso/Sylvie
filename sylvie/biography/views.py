from django.shortcuts import render

# Create your views here.

def renderBiography(request):
    return render(request, "biography.html")