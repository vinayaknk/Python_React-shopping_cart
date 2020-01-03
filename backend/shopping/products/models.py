from django.db import models

# Create your models here.

class Product(models.Model):
    productId = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    value = models.IntegerField()

    def __str__(self):
        return self.name

class Offer(models.Model):
    code = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.discount


