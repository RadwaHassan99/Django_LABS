from django.urls import path
from .views import index
from . import views

app_name = "book_store"
urlpatterns = [
    path("", views.index, name="home-index"),
    path("books/create", views.create, name="home-create"),
    path("books/store", views.store, name="home-store"),
    path("books/<int:id>/edit", views.edit, name="home-edit"),
    path("books/<int:id>", views.show, name="home-show"),
    path("books/<int:id>/delete", views.destroy, name="home-destroy"),
    path("books/<int:id>/update", views.update, name="home-update"),
]