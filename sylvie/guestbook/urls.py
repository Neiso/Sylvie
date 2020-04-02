from django.urls import path
from .views import renderGuestbook, addMessage

urlpatterns = [
    path('guestbook/', renderGuestbook),
    path('guestbook/addMessage', addMessage),
]