from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name