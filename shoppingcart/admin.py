from django.contrib import admin

from .models import Item, Cart, CartItem

# Register your models here.
admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Cart)