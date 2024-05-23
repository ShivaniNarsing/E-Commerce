from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=25)
    number=models.IntegerField(max_length=10)
    cost=models.IntegerField(max_length=10)
    