from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    poids = models.FloatField()
    prix_reel = models.FloatField()
    prix_estime = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nom
