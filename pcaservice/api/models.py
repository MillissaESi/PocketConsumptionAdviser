from django.db import models


# Create your models here.

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
