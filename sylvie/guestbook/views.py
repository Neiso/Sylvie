from django.shortcuts import render
from .models import Commentaire

# Create your views here.

def renderGuestbook(request):
    # comment = Commentaire.object
    # comment.exist = False
    return render(request, 'guestbook.html')#, {'comments': comment})

def addMessage(request):
    new_comment = Commentaire()
    new_comment.name = request.GET['name']
    new_comment.email = request.GET['email']
    new_comment.comment = request.GET['commentaire']
    new_comment.exist = True
    new_comment.save()
    return render(request, 'guestbook.html', {'comments': [new_comment]})