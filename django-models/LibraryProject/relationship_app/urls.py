from django.urls import path
from .views import list_books, LibraryDetailView
views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
