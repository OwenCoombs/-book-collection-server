from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    genre = serializers.CharField(source='genre.name')

    class Meta:
        model = Book
        fields = ['id','title', 'author', 'genre']

    def create(self, validated_data):
    # Extract author and genre data from validated data
        author_name = validated_data.pop('author')['name']
        genre_name = validated_data.pop('genre')['name']

    # Retrieve existing author from database or create a new one if not found
        author, created = Author.objects.get_or_create(name=author_name)
    
    # Retrieve existing genre from database or create a new one if not found
        genre, created = Genre.objects.get_or_create(name=genre_name)

    # Create a new book instance with extracted data and associations
        book = Book.objects.create(author=author, genre=genre, **validated_data) # kinda like ...
    
    # Return the newly created book instance
        return book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class Genreserializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'