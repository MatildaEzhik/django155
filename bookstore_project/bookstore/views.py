from django.shortcuts import render, get_object_or_404, redirect

from bookstore.forms import AuthorForm, CategoryForm, BookForm
from bookstore.models import Author, Category, Book

def index(request):
    return render(request, 'bookstore/index.html')


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'bookstore/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'bookstore/author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'bookstore/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'bookstore/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'bookstore/author_confirm_delete.html', {'author': author})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'bookstore/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'bookstore/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'bookstore/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'bookstore/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'bookstore/category_confirm_delete.html', {'category': category})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookstore/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookstore/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookstore/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookstore/book_confirm_delete.html', {'book': book})