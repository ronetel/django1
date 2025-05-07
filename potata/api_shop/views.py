from django.shortcuts import render
from .serializers import *
from shop_project.models import *
from .permission import *
from rest_framework import viewsets
# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ProductInCheckViewSet(viewsets.ModelViewSet):
    queryset = ProductInCheck.objects.all()
    serializer_class = ProductInCheckSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
