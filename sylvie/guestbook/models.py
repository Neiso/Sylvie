from django.db import models

# Create your models here.

class Commentaire(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length = 51)
    email = models.CharField(max_length = 51)
    comment = models.CharField(max_length = 600)

    objects = models.Manager()

    def __str__(self):
        return self.name