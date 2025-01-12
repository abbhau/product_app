from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    prize  = models.FloatField()
    total_prize = models.FloatField( default=0)
    brand = models.ManyToManyField(Brand, blank=True)

    def __str__(self):
        return self.name


