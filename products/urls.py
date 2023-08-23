from django.urls import path
from products.views import ProductsViews

create_list_product = ProductsViews.ProductListCreateAPIView.as_view()
product_detail = ProductsViews.ProductDetailDeleteUpdateAPIView.as_view()

urlpatterns = [
    path('list-create-product/', create_list_product, name='create_list_product'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
]