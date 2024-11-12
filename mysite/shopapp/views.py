import logging

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from shopapp.models import Book

log = logging.getLogger(__name__)


class ShopIndexView(TemplateView):
    template_name = "shopapp/index.html"
    log.info("Рендеринг главной страницы")


class ProductCreateView(CreateView):
    template_name = "shopapp/product-create.html"


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "shopapp/register.html")


def book_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    total_books = books.count()
    context = {"books": books, "total_books": total_books}
    return render(request, "shopapp/book_list.html", context=context)
