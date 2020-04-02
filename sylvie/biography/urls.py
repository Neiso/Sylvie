from django.urls import path
from .views import renderBiography

urlpatterns = [
    path('', renderBiography),
]