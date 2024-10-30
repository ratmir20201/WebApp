from django.http import HttpResponse
from django.shortcuts import render


def shop_index(request):
    return render(request, 'shopapp/index.html')


def user_room(request):
    context = {
        "name": "Пётр",
        "email": "some@gmail.com",
        "phone": 87779998888
    }
    return render(request, 'shopapp/user_room.html', context=context)


def product_create(request):
    return render(request, 'shopapp/product-create.html')


def register(request):
    return render(request, 'shopapp/register.html')
