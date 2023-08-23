from rest_framework import serializers
from cart.models import CartModel, CartItemModel
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = CartModel
        fields = '__all__'

    def get_products(self, obj) -> dict:
        products = obj.products.all()
        return ProductSerializer(products, many=True).data