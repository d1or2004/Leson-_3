from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics
from rest_framework.response import Response


# class BookListAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreatesAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.save()
            data = {
                'book': book
            }
            return Response(data)


# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailAPIView(APIView):
    def get(self, pk):
        book = Book.objects.get(pk=pk)
        serializer_data = BookSerializer(book).data

        data = {
            'book': serializer_data
        }
        return Response(data)


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def book_list(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
