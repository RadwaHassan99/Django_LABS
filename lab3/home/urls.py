from django.urls import path
from .views import *
from . import views

app_name = "lab3"
urlpatterns = [
    path('',  index, name="book-index"),
    path("books/create", create, name="book-create"),
    path("books/store", store, name="book-store"),
    path("books/<int:id>", show, name="book-show"),
    path("books/<int:id>/delete", destroy, name="book-delete"),
    path("books/<int:id>/update", update, name="book-update"),
    path("books/<int:id>/edit", edit, name="book-edit")

]