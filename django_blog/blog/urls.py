# django_blog/blog/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('posts/<int:pk>/comments/add/', views.add_comment, name='add-comment'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/edit/', views.edit_comment, name='edit-comment'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete-comment'),

    # Auth
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Search & tags
    path('search/', views.search, name='search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='tag-posts'),
]
