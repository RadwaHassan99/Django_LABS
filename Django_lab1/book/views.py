from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'main/base_layout.html')


books_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'book-1',
        'priority': 1,
        'description': "Learning Learnin gJSfffjk dfjdklg jkdgjdkgjdkgjd kgjdkgjdglk jdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgek",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'book-2',
        'priority': 4,
        'description': "Learning LearningJS fffjkdfjd klgjkdgjdkgjdkgjdkgjd kgjdglkjdgk ljfj fjejekgjekgjekgjekgjgekjgek",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'book-3',
        'priority': 2,
        'description': "LearningJS fffjk dfjdklgjkdg jdkgjdkgjd kgjdkgjdglkjdgkl jfjfjejekg jekgjekgjekgjgekjgek",
    },
]


def _get_book(book_id):
    for book in books_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None
    
def book_list(request):
    my_context = {'book_list': books_list}
    return render(request, 'book/book_list.html', context=my_context)



def book_detail(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    my_context = {
        'book_id': book_object.get('id'),
        'book_name': book_object.get('name'),
        'book_priority': book_object.get('priority'),
        'book_description': book_object.get('description')
    }

    return render(request, 'book/book_details.html', context=my_context)


def book_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    if books_list:
        books_list.remove(book_object)
    return redirect('book:book-list')   

def book_update(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    for book in books_list:
        if book == book_object:
            book['name'] = f"Update {book_object['name']}"
            
    return redirect('book:book-list') 
