from django.db import models

class mobiles(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    band = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    rating=models.FloatField(null=True,default=3)