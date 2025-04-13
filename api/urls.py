from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet,CategoryViewSet,ReviewViewSet,ProductImageViewSet
from rest_framework_nested import routers
from order.views import CartViewSet,CartItemViewSet,OrderViewSet

router = routers.DefaultRouter()

router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')
router.register('orders', OrderViewSet, basename='orders')


product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
product_router.register('images', ProductImageViewSet, basename='product-image')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

