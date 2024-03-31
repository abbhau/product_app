from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    prize  = models.FloatField()
    total_prize = models.FloatField( default=0)

