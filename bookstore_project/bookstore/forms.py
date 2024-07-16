from django import forms

from bookstore.models import Author, Category, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'photo', 'biography']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'authors', 'categories']
