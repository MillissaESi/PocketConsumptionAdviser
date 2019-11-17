from django.db import models


# Create your models here.

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Costumer(models.Model):
    objects = None
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Question(models.Model):
    objects = None
    body = models.CharField(max_length=255)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    concerned = models.ForeignKey(Costumer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Answer(models.Model):
    objects = None
    # Yes or NO
    answer = models.CharField(max_length=255)

    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
