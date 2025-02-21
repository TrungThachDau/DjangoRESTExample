from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Book
from rest_framework import permissions, viewsets
from .serializers import BookSerializer
# Create your views here.
# def books(request):
#     #get list books
#     books_list = Book.objects.all()
#     return render(request, 'books.html', {'books': books_list})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
