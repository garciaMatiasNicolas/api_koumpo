from django.urls import path
from cart.views.views_cart import CartViews
from cart.views.views_cartitem import CartItemViews

# Cart views
create_cart = CartViews.CartCreateAPIView.as_view()
detail_cart = CartViews.CartDetailAPIView.as_view()

# Cart Item views
create_cart_item = CartItemViews.CartItemCreateAPIView.as_view()
detail_cart_item = CartItemViews.CartItemDetailAPIView.as_view()

urlpatterns = [
    # Urls for Cart Views
    path('create-cart/', create_cart, name='create_cart'),
    path('detail-cart/<int:pk>/', detail_cart, name='detail_cart'),

    # Urls for CartItem Views
    path('create-cart-item/', create_cart_item, name='create_cart_item'),
    path('detail-cart-item/<int:pk>/', detail_cart_item, name='detail_cart_item')
]