from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import path
from .views import admin_view, librarian_view, member_view
from django.urls import path
from .views import add_book, edit_book, delete_book
urlpatterns = [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),,
views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=[
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
add_book/", "edit_book/
