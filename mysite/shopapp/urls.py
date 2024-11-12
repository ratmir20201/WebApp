from django.urls import path

from shopapp.views import (
    ShopIndexView,
    ProductCreateView,
    book_list,
)

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/", book_list, name="book_list"),
]
