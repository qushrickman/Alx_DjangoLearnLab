from django.db import models

# Author model represents a writer.
# One author can have many books (One-to-Many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)  # Stores the author's full name

    def __str__(self):
        return self.name


# Book model represents a book written by an Author.
# Each book has a title, publication year, and is linked to one Author.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()   # Year the book was published
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )  # Foreign key establishes the one-to-many relationship

    def __str__(self):
        return self.title
