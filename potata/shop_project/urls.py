from django.urls import include, path
from .views import *

urlpatterns = [
    path('base', base_view, name='base'),
    path('contacts', contacts_view, name='contacts'),
    path('find-us', find_us_view, name='find-us'),
    path('product', products_view, name='product'),
    path('categories', categories_view, name='categories'),
    path('cart', cart_view, name='cart'),

    path("__reload__/", include("django_browser_reload.urls")),

    path('producttypes/', ProductTypeListView.as_view(), name='producttype_list'),
    path('producttypes/<int:pk>/', ProductTypeDetailView.as_view(), name='producttype_detail'),
    path('producttypes/new/', ProductTypeCreateView.as_view(), name='producttype_create'),
    path('producttypes/<int:pk>/edit/', ProductTypeUpdateView.as_view(), name='producttype_update'),
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype_delete'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/new/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    path('stocks/', StockListView.as_view(), name='stock_list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('stocks/new/', StockCreateView.as_view(), name='stock_create'),
    path('stocks/<int:pk>/edit/', StockUpdateView.as_view(), name='stock_update'),
    path('stocks/<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),

    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail'),
    path('ingredients/new/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/<int:pk>/edit/', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient_delete'),
]
