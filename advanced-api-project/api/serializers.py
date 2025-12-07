from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for the Book model
# Includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validator to prevent future publication years
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# Author serializer with nested list of all books written by the author.
# Uses BookSerializer to serialize related Book objects.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested relationship

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
