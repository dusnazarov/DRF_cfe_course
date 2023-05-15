# 1) ////////////// ModelViewSet  ////////////////////////////
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register("products-abc", ProductViewSet, basename='products')

urlpatterns = router.urls


# 2) //////////////////  GenericViewSet   ////////////////////////
# from rest_framework.routers import DefaultRouter
# from products.viewsets import ProductGenericViewSet

# router = DefaultRouter()
# router.register("products", ProductGenericViewSet, basename='products')

# # print(router.urls)
# urlpatterns = router.urls
