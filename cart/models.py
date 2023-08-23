from django.db import models
from simple_history.models import HistoricalRecords
from users.models import UserModel
from products.models import ProductModel


class CartModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, through='CartItemModel')
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f'Id cart: {self.id}, Owner: {self.user.first_name} {self.user.last_name}'


UserModel.carts = models.ManyToManyField(CartModel)


class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f'{self.product.name}'