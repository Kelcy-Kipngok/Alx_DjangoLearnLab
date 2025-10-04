# django_blog/blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Tag

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

class PostForm(forms.ModelForm):
    # Optionally allow comma-separated tag names on form
    tag_names = forms.CharField(
        required=False,
        help_text='Comma-separated tags (optional).',
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag_names']

    def save(self, commit=True):
        # Custom save to handle tag_names
        tag_names = self.cleaned_data.pop('tag_names', '')
        post = super().save(commit=commit)
        if tag_names:
            names = [t.strip() for t in tag_names.split(',') if t.strip()]
            from .models import Tag
            for name in names:
                tag_obj, _ = Tag.objects.get_or_create(name=name)
                post.tags.add(tag_obj)
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }
