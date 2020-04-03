from django.db import models

# Create your models here.

class ExpoModel (models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='expo')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)