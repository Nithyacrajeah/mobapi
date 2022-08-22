from django.db import models

# Create your models here.
class mobiles(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    band = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    price=models.PositiveIntegerField()