# CREATE
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984 by George Orwell>

# RETRIEVE
>>> Book.objects.get(title="1984")
# Output: <Book: 1984 by George Orwell>

# UPDATE
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
# Output: <Book: Nineteen Eighty-Four by George Orwell>

# DELETE
>>> book.delete()
# Output: (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# Output: <QuerySet []>
