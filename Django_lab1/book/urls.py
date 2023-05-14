from django.urls import path
from .views import index, book_list, book_detail, book_delete, book_update

app_name = 'book'


urlpatterns = [
    path('index', index, name='book-index'),
    path('book_list/', book_list, name="book-list"),
    path('book_detail/<int:book_id>', book_detail, name="book-detail"),
    path('book_delete/<int:book_id>', book_delete, name="book-delete"),
    path('book_update/<int:book_id>', book_update, name="book-update")
]
