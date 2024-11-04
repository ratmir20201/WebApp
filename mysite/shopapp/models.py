from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False, blank=True)
    price = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def short_description(self):
        if len(self.description) < 50:
            return self.description
        return self.description[:50] + "..."

    def __str__(self):
        return "Продукт: {product}".format(
            product=self.name
        )


class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=False)
    promocode = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
