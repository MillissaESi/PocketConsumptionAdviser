from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Product, Answer, Question, Costumer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all().order_by('firstname')
    serializer_class = ProductSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = ProductSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = ProductSerializer
