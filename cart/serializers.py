from rest_framework import serializers
from cart.models.model_cart import CartModel
from cart.models.model_cart_item import CartItemModel
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItemModel
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': self.instance.id,
            'user': self.instance.user.id,
            'cart_items': self.instance.cart_items.all()
        }