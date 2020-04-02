from django.contrib import admin
from .models import Commentaire

# Admin visual custom

admin.site.site_header = "C'est tout uN ARt Oh!"

# Register your models here.

class CommentaireAdmin (admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'comment', 'status']
    list_filters = ['name', 'date']

    actions = ['publish_selected', 'remove_selected']

    def publish_selected(self, request, queryset):
        queryset.update(status = True)
    publish_selected.short_description = "Publier les commentaires sélectionnés"
    def remove_selected(self, request, queryset):
        queryset.update(status = False)
    remove_selected.short_description = "Retirer les commentaires sélectionnés"

admin.site.register(Commentaire, CommentaireAdmin)
