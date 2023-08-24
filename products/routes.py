from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

router = DefaultRouter()

router.register('', ProductViewSet, basename='products')

urlpatterns = router.urls