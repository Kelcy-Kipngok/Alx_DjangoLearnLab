from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
"from django_filters import rest_framework"
"from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"
# -----------------------------
# LIST + CREATE
# -----------------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles GET (list all books) and POST (create new book).
    - Anyone can view
    - Only authenticated users can create
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
"ListView", "UpdateView", "DeleteView"

# -----------------------------
# DETAIL + UPDATE + DELETE
# -----------------------------
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (single book), PUT/PATCH (update), DELETE (remove).
    - Anyone can view
    - Only authenticated users can update/delete
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
 function filters.ordering filter 
"filter.Searchfilter"
"filters.OrderingFilter"
"filters.SearchFilter"
# Create your views here.







