from django.db import models

# Create your models here.

class Commentaire(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 51)
    email = models.CharField(max_length = 51, blank=True)
    comment = models.CharField(max_length = 600)
    status = models.BooleanField(default = False)

    list_display = ('date', 'comment')

    def __str__(self):
        return self.name