from django.db import models
from products.models import ProductModel
from users.models import UserModel
from simple_history.models import HistoricalRecords

class CartModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField('CartItemModel', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f'Id cart: {self.id}, Owner: {self.user.first_name} {self.user.last_name}'

    def get_product_data(self):
        return [{'id': item.product.id, 'name': item.product.name, 'quantity': item.quantity} for item in
                self.products.all()]

UserModel.carts = models.ManyToManyField(CartModel)


