from .models import *
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'objects', 'title', 'author', 'yearOfRel', 'genre', 'category', 'publisher', 'photoPreview', 'bookFile']


    def create(self, validated_data):
         return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
         instance.id = validated_data.get('id', instance.id)
         instance.objects = validated_data.get('objects', instance.objects)
         instance.title = validated_data.get('title', instance.title)
         instance.author = validated_data.get('author', instance.author)
         instance.yearOfRel = validated_data.get('yearOfRel', instance.yearOfRel)
         instance.genre = validated_data.get('genre', instance.genre)
         instance.category = validated_data.get('category', instance.category)
         instance.publisher = validated_data.get('publisher', instance.publisher)
         instance.photoPreview = validated_data.get('photoPreview', instance.photoPreview)
         instance.bookFile = validated_data.get('bookFile', instance.bookFile)

         return instance

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'lastName', 'middle_name', 'dateOfBirth']

    def create(self, validated_data):
         return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
         instance.name = validated_data.get('name', instance.name)
         instance.lastName = validated_data.get('lastName', instance.lastName)
         instance.middle_name = validated_data.get('middle_name', instance.middle_name)
         instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)

         return instance