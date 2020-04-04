from django.contrib import admin
from django import forms
from .models import Peinture, Categorie

# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class PeintureAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'style',
        'categorie'
    ]

admin.site.register(Peinture, PeintureAdmin)
admin.site.register(Categorie)#, CategorieAdmin)
