from django.urls import include, path
from .views import *

urlpatterns = [
    path('base', base_view, name='base'),
    path('contacts', contacts_view, name='contacts'),
    path('find-us', find_us_view, name='find-us'),
    path('products', products_view, name='products'),
    path('categories', categories_view, name='categories'),
    path('cart', cart_view, name='cart'),

    path("__reload__/", include("django_browser_reload.urls")),

]
