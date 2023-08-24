from rest_framework.routers import DefaultRouter
from cart.views.views_cart import CartViewSets
from cart.views.views_cartitem import CartItemViewSets

router = DefaultRouter()

router.register('cart', CartViewSets, basename='cart')
router.register('cart-item', CartItemViewSets, basename='cart_item')

urlpatterns = router.urls