from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    age = models.IntegerField()
    profile_pic = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name
