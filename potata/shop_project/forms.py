from django import forms
from .models import *

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'img', 'product_type']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'adress']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'supplier', 'stock', 'img', 'quantity']
