from django.shortcuts import render
from .models import Commentaire
from django.conf import settings

# Create your views here.

def renderGuestbook(request):
    rawData = Commentaire.objects.order_by('-date')
    return render(request, 'guestbook.html', {'comments': rawData})

def addMessage(request):
    new_comment = Commentaire()
    new_comment.name = request.GET['name']
    new_comment.email = request.GET['email']
    new_comment.comment = request.GET['commentaire']
    new_comment.save()
    rawData = Commentaire.objects.all()
    return render(request, 'guestbook.html', {'comments': rawData})