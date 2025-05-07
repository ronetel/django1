from .views import *
from rest_framework import routers

urlpatterns = [
     
]

router = routers.SimpleRouter()
router.register('producttypes', ProductTypeViewSet, basename='productrypes')
router.register('products', ProductsViewSet, basename='product')
router.register('stocks', StockViewSet, basename='stocks')
router.register('suppliers', SupplierViewSet, basename='suppliers')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('orders', OrderViewSet, basename='orders')
router.register('productincheck', ProductInCheckViewSet, basename='productincheck')
urlpatterns += router.urls