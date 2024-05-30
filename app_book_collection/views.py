from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)


@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
        password = request.data['password']
    )
    user.save()
    profile = Profile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    print(request)
    books = Book.objects.all()
    serialized_books = BookSerializer(books, many=True)
    return Response(serialized_books.data)
    # return Response(serialized_book.data)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([])  # Adjust permission classes as needed
def book_list(request):
    # Handle GET request to fetch all books
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    # Handle POST request to create a new book
    elif request.method == 'POST':
        # Deserialize the request data into a Book object
        serializer = BookSerializer(data=request.data)
        # Validate the deserialized data
        if serializer.is_valid(): # Save the validated data to the database
            serializer.save()
            return Response(serializer.data)
    
    # Handle DELETE request to delete a book
    elif request.method == 'DELETE':
        # Get the book ID from request data
        book_id = request.data.get('id')
        # Query the book from the database
        book = Book.objects.get(id=book_id)
        # Delete the book from the database
        book.delete()
            






class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = Genreserializer


