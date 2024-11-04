from django.contrib import admin
from .models import Book, Product, Order


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    list_filter = ('author', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'short_description', 'price', 'discount', 'created_at'
    )
    list_display_links = ('name', )
    list_filter = ('name', )

admin.site.register(Book, BookAdmin)