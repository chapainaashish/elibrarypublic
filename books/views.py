from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from .forms import BookForm


def book_read(request):
    books = Books.objects.all()
    return render(request, "books/book_read.html", {"books": books})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_read")
        else:
            return render(request, "message.html")
    elif request.method == "GET":
        form = BookForm()
        return render(request, "books/book_create.html", {"form": form})


def book_update(request, book_id):
    try:
        book = Books.objects.get(pk=book_id)
    except Books.DoesNotExist:
        return render(request, "books/book_not_exist.html")

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_read")
        else:
            return render(request, "message.html")

    elif request.method == "GET":
        form = BookForm(
            {
                "title": book.title,
                "author": book.author,
                "description": book.description,
            }
        )
        return render(
            request,
            "books/book_create.html",
            {"form": form, "book": book},
        )


def book_delete(request, book_id):
    try:
        book = Books.objects.get(pk=book_id)
    except Books.DoesNotExist:
        return render(request, "books/book_not_exist.html", {"book_id": book_id})

    book.delete()
    return render(
        request,
        "books/book_delete.html",
        {"book_title": book.title},
    )
