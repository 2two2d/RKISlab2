from .models import *
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['objects', 'title', 'author', 'yearOfRel', 'genre', 'category', 'publisher', 'photoPreview', 'bookFile']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.yearOfRel = validated_data.get('yearOfRel', instance.yearOfRel)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.category = validated_data.get('category', instance.category)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.photoPreview = validated_data.get('photoPreview', instance.photoPreview)
        instance.bookFile = validated_data.get('bookFile', instance.bookFile)



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'lastName', 'middle_name', 'dateOfBirth']
