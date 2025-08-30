from django.contrib import admin
from .models import Book

# Basic registration (if no customization is needed)
# admin.site.register(Book)

# With customization:
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    list_filter = ('publication_year', 'author')            # Filters on the right sidebar
    search_fields = ('title', 'author')                     # Search functionality
