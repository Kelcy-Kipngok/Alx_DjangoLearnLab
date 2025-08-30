from bookshelf.models import Book

# Update the book's title
book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
book.title
