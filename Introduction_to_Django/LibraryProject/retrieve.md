from bookshelf.models import Book

# Retrieve all books
book = Book.objects.first()
book.title, book.author, book.publication_year
