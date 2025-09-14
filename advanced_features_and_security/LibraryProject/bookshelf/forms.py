# bookshelf/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "summary", "isbn"]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 4}),
        }
"ExampleForm"
    # Example of cleaning: enforce a reasonable title length
    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        if len(title) > 255:
            raise forms.ValidationError("Title too long.")
        return title

class BookSearchForm(forms.Form):
    q = forms.CharField(required=True, max_length=100)

    def clean_q(self):
        q = self.cleaned_data["q"].strip()
        # Additional sanitization/logic as needed
        return q
