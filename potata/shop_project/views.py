from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'base.html')
def contacts_view(request):
    return render(request, 'contacts.html')
def find_us_view(request):
    return render(request, 'find-us.html')
def products_view(request):
    return render(request, 'products.html')
def categories_view(request):
    return render(request, 'categories.html')
def cart_view(request):
    return render(request, 'cart.html')


