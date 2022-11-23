from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

def index(request):
    return render(request, 'main.html')


@csrf_exempt
def book_list(request):
   """
   List all code snippets, or create a new snippet.
   """
   if request.method == 'GET':
       books = Book.objects.all()
       serializer = BookSerializer(books, many=True)
       return JsonResponse(serializer.data, safe=False)

   elif request.method == 'POST':
       data = JSONParser().parse(request)
       serializer = BookSerializer(data=data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=201)
       return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book_detail(request, pk):
   """
   Retrieve, update or delete a code snippet.
   """
   try:
       book = Book.objects.get(id=pk)
   except Book.DoesNotExist:
       return HttpResponse(status=404)

   if request.method == 'GET':
       serializer = BookSerializer(book)
       return JsonResponse(serializer.data)

   elif request.method == 'PUT':
       data = JSONParser().parse(request)
       serializer = BookSerializer(book, data=data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data)
       return JsonResponse(serializer.errors, status=400)

   elif request.method == 'DELETE':
       book.delete()
       return HttpResponse(status=204)

@csrf_exempt
def author_list(request):
   """
   List all code snippets, or create a new snippet.
   """
   if request.method == 'GET':
       authors = Author.objects.all()
       serializer = AuthorSerializer(authors, many=True)
       return JsonResponse(serializer.data, safe=False)

   elif request.method == 'POST':
       data = JSONParser().parse(request)
       serializer = AuthorSerializer(data=data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=201)
       return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def author_detail(request, pk):
   """
   Retrieve, update or delete a code snippet.
   """
   try:
       author = Author.objects.get(id=pk)
   except Author.DoesNotExist:
       return HttpResponse(status=404)

   if request.method == 'GET':
       serializer = AuthorSerializer(author)
       return JsonResponse(serializer.data)

   elif request.method == 'PUT':
       data = JSONParser().parse(request)
       serializer = AuthorSerializer(author, data=data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data)
       return JsonResponse(serializer.errors, status=400)

   elif request.method == 'DELETE':
       author.delete()
       return HttpResponse(status=204)