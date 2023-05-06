from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
]