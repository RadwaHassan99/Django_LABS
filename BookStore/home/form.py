from django.forms import ModelForm
from .models import Book
from django import forms

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author_name', 'genre', 'title', 'description', 'rate', 'views']
        widgets = {
            'author_name': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Enter genre'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
            'rate': forms.NumberInput(attrs={'placeholder': 'Enter rate'}),
            'views': forms.NumberInput(attrs={'placeholder': 'Enter views'}),
        }
