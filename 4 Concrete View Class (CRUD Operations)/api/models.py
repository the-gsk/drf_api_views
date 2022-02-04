from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    def __str__(self):
        return self.name