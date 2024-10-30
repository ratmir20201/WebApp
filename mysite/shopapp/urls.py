from django.urls import path

from shopapp.views import (
    shop_index,
    user_room,
    product_create,
    register,
)

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("user-room/", user_room, name="user_room"),
    path("product-create/", product_create, name="product_create"),
    path("register/", register, name="register"),
]
