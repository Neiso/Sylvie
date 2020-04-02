from django.contrib import admin
from .models import Commentaire

# Admin visual custom

admin.site.site_header = "C'est tout uN ARt Oh!"

# Register your models here.

class CommentaireAdmin (admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'comment', 'status']
    list_filters = ['name', 'date']

admin.site.register(Commentaire, CommentaireAdmin)
