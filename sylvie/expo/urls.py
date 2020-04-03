from django.urls import path
from .views import renderExpo

urlpatterns = [
    path('expo/', renderExpo)
]