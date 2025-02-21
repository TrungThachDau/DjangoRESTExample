from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .models import TypeBook
from rest_framework import permissions, viewsets, status
from .serializers import BookSerializer, TypeBookSerializer
# Create your views here.
# def books(request):
#     #get list books
#     books_list = Book.objects.all()
#     return render(request, 'books.html', {'books': books_list})
@api_view(['GET'])
def GetAllTypeBook(request):

    typebooks = TypeBook.objects.all()
    serializer = TypeBookSerializer(typebooks, many=True)
    return Response(serializer.data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TypeBookList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        try:
            typebook = TypeBook.objects.all()
            serializer = TypeBookSerializer(typebook, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e)


class BookUpdateView(APIView):
    def UpdateBook(self, request, id):
        try:
            your_model = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(your_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

