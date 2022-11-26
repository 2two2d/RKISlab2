from .models import *
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'objects', 'title', 'author', 'yearOfRel', 'genre', 'category', 'publisher', 'photoPreview', 'bookFile']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'lastName', 'middle_name', 'dateOfBirth']
