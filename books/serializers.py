from rest_framework import serializers
from .models import Book
from .models import TypeBook

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'pub_date','type_id']

class TypeBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeBook
        fields = ['id', 'name']