from rest_framework import serializers
from shop_project.models import ProductType, Product, Supplier, Stock, Ingredient, Recipe, Order, ProductInCheck

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'img', 'product_type']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'adress']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'supplier', 'stock', 'img', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['product', 'ingredient']

class ProductInCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCheck
        fields = ['order', 'product', 'count']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['comment', 
                  'delivery_adress', 
                  'delivery_type', 
                  'date', 
                  'date_finish',
                  'products'
                  ]
