from django.urls import path
from .views import renderStyle

urlpatterns = [
    path('aquarelles', renderStyle, {'style_name':'Aquarelles'}),
    path('encres', renderStyle, {'style_name':'Encres'}),
    path('acryliques', renderStyle, {'style_name':'Acryliques'}),
    path('huiles', renderStyle, {'style_name':'Huiles'}),
    path('demos', renderStyle, {'style_name':'Demos'}),
]