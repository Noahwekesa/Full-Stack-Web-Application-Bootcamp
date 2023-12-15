from django.db import models

# Create your models here.

class Shirts(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=150, null = True)
    brand = models.CharField(max_length=50, null= True)
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length= 70)
    description = models.TextField(max_length=150)
    category = models.CharField(max_length=50)
    image = models.ImageField(blank =True, upload_to='product-img')
    brand = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__ (self):
        return self.title
