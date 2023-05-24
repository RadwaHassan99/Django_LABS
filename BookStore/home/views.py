from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from home.models import Book
from .form import BookForm

def index(request):
    """
    Returns a rendered HTML template displaying a list of books.

    Parameters:
    request: the HTTP request object

    Returns:
    a rendered HTML response containing a list of books

    """
    books = Book.objects.all().values()
    return render(request, "home/index.html", {"books": books})


def show(request, id):
    """
    Returns a rendered HTML template displaying the details of a specific book.

    Parameters:
    - request: the HTTP request object
    - id: the ID of the book to display

    Returns:
    - a rendered HTML response containing the details of the specified book

    """

    book = Book.objects.get(pk=id)
    return render(request, "home/show.html", {"book": book})


def edit(request, id):
    """
    Returns A rendered HTML template displaying form to edit specific book

    Parameters:
    - request: HTTP request object
    - id: the ID of the book to edit

    Returns:
    - A rendered HTML response containing form to edit a specified book

    """

    book = Book.objects.get(pk=id)
    form = BookForm(instance=book)
    return render(request, "home/edit.html", {'form':form , 'book':book})


def create(request):
    """
    Returns a rendered HTML template displaying the form to create bew book.

    Parameters:
    - request: the HTTP request object

    Returns:
    - a rendered HTML response containing the book form 

    """
    
    form = BookForm()
    return render(request, "home/create.html" , {"form" : form})


def store(request):

    """
    Store Book Data in Database and redirect to home page.

    Parameters:
    - request: the HTTP request object

    Returns:
    - redirect to home page 

    """

    form = BookForm(request.POST)
    if form.is_valid:
       form.save()
    return redirect('book_store:home-index')


@csrf_protect
def update(request, id):

    """
    Update Book Data in Database and redirect to home page.

    Parameters:
    - request: the HTTP request object
    - id: the ID of the book to update

    Returns:
    - redirect to home page 

    """

    book = Book.objects.get(pk=id)
    form = BookForm(request.POST , instance=book)
    if form.is_valid:
        form.save()

    return redirect("book_store:home-index")


def destroy(request, id):
    """
    Deletes a specific book instance.

    Parameters:
    - request: the HTTP request object
    - pk: the primary key of the book to delete

    Returns:
    - a redirect to the home page
    """

    book = Book.objects.get(pk=id)
    book.delete()
    return redirect("book_store:home-index")