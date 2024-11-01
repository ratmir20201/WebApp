from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from shopapp.models import Book


def shop_index(request:  HttpRequest) -> HttpResponse:
    return render(request, 'shopapp/index.html')

def user_room(request:  HttpRequest) -> HttpResponse:
    context = {
        "name": "Пётр",
        "email": "some@gmail.com",
        "phone": 87779998888
    }
    return render(request, 'shopapp/user_room.html', context=context)

def product_create(request:  HttpRequest):
    return render(request, 'shopapp/product-create.html')

def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'shopapp/register.html')

def book_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    total_books = books.count()
    context = {
        'books': books,
        'total_books': total_books
    }
    return render(request, 'shopapp/book_list.html', context=context)
