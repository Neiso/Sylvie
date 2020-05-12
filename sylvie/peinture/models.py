from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.name

class Peinture(models.Model):
    ACRYLIQUES = 'Acryliques'
    ENCRES = 'Encres'
    HUILES = 'Huiles'
    AQUARELLES = 'Aquarelles'
    DEMOS = 'Demos'
    GROUPE=[
        (AQUARELLES,'Aquarelles'),
        (ACRYLIQUES, 'Acryliques'),
        (ENCRES, 'Encres'),
        (HUILES, 'Huiles'),
        (DEMOS, 'Demos'),
    ]

    name = models.CharField(max_length=100, blank=True)
    
    categorie = models.ForeignKey(Categorie, default=None, on_delete=models.CASCADE, editable=True)
    
    style = models.CharField(
        default=AQUARELLES,
        choices=GROUPE,
        max_length=50)
    
    photo = models.ImageField(upload_to='peintures')
    
    desc = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
