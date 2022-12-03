from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from .models import *
from .serializers import BookSerializer, AuthorSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status, permissions
from .permissions import IsAdminOrReadOnly
# Create your views here.

def index(request):
    return render(request, 'main.html')

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            if (Book.objects.get(title=request.data['title']).publisher != request.data['publisher'] and request.data[
                'genre'] == 'художественное произведение, переведенное с другого языка'):
                serializer.is_valid()
            if (Book.objects.get(title=request.data['title']).yearofRel != request.data['yearOfRel'] and request.data[
                'genre'] == 'учебник'):
                serializer.is_valid()
            else:
                raise Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Book.objexts.get(pk=pk)
        except:
            return Response({'error':'Объект не найден'})

        serializer = BookSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)






class BookDetail(APIView):

    def get(self, request, pk):
        books = Book.objects.get(pk=pk)
        serializer = BookSerializer(books)
        return Response(serializer.data)

class BookFind(APIView):

    def get(self, request, field, property):
        try:
            if field == 'title':
                books = Book.objects.filter(title=property)
            elif field == 'genre':
                books = Book.objects.filter(genre=property)
            elif field == 'author':
                books = Book.objects.filter(author=property)
        except Book.DoesNotExist:
            return HttpResponse(status=404)


        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class AuthorList(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(APIView):

    def get(self, request, pk):
        authors = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data)