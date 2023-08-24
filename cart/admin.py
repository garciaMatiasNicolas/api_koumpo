from django.contrib import admin
from cart.models.model_cart import CartModel
from cart.models.model_cart_item import CartItemModel

# Register your models here.
admin.site.register(CartModel)
admin.site.register(CartItemModel)