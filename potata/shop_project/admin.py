from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductInCheck)
class ProductInCheckAdmin(admin.ModelAdmin):
    pass