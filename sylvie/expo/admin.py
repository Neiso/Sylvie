from django.contrib import admin
from .models import ExpoModel

# Register your models here.

class ExpoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'date']

admin.site.register(ExpoModel, ExpoModelAdmin)