from rest_framework import serializers
from datetime import date
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):

    #Serializer for the Book model.
    #Includes validation to ensure publication year is not in the future.

    class Meta:
        model = Book
        fields = '__all__'

    
        #Validates that the publication year is not in the future.

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError('Publication year cannot be in future. ')
        return value
        

class AuthorSerializer(serializers.ModelSerializer):
    #Serializer for the Author model.
    #Converts Author instances to and from JSON representations.
    #Has a nested serializer to serialize the realted books dynamically.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']