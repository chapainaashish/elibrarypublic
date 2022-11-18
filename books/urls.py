from django.urls import path
from . import views


urlpatterns = [
    path("", views.book_read, name="book_read"),
    path("create/", views.book_create, name="book_create"),
    path("update/<int:book_id>", views.book_update, name="book_update"),
    path("delete/<int:book_id>", views.book_delete, name="book_delete"),
]
