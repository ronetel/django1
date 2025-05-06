from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название типа продукта'
            }),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'img', 'product_type']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название продукта'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите цену'
            }),
            'img': forms.FileInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'accept': 'image/*'
            }),
            'product_type': forms.Select(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            }),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'adress']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название поставщика'
            }),
            'adress': forms.TextInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите адрес'
            }),
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название склада'
            }),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'supplier', 'stock', 'img', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название ингредиента'
            }),
            'supplier': forms.Select(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            }),
            'stock': forms.Select(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            }),
            'img': forms.FileInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'accept': 'image/*'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите количество'
            }),
        }

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        min_length=2
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        min_length=2
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
    )
