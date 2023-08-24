from django.db import models
from products.models import ProductModel
from .model_cart import CartModel
from simple_history.models import HistoricalRecords

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f'{self.product.name}'