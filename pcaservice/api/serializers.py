from rest_framework import serializers
from .models import Product, Costumer, Question, Answer


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class CostumerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Costumer
        fields = ['firstname', 'lastname']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(many=False, required=False)
    concerned = CostumerSerializer(many=False)

    class Meta:
        model = Question
        fields = ['body', 'product', 'concerned']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer(many=False)

    class Meta:
        model = Answer
        fields = ['answer', 'question']
