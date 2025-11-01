from django.db import models

# Create your models here.
class Produit(models.Model):
    nom         = models.TextField()
    description = models.TextField()
    prix        = models.TextField()
    active      = models.TextField(default='valeur par defaut')