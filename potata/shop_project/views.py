from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required 
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

# Create your views here.
def main_view(request):
    return render(request, 'main.html')
def contacts_view(request):
    return render(request, 'contacts.html')
def find_us_view(request):
    return render(request, 'find-us.html')
def products_view(request):
    return render(request, 'product.html')
def categories_view(request):
    return render(request, 'categories.html')
def cart_view(request):
    return render(request, 'cart.html')

class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'producttypes/producttype_list.html'
    context_object_name = 'producttypes'

class ProductTypeDetailView(DetailView):
    model = ProductType
    template_name = 'producttypes/producttype_detail.html'

class ProductTypeCreateView(CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'producttypes/producttype_form.html'
    success_url = reverse_lazy('producttype_list')

class ProductTypeUpdateView(UpdateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'producttypes/producttype_form.html'
    success_url = reverse_lazy('producttype_list')

class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'producttypes/producttype_delete.html'
    success_url = reverse_lazy('producttype_list')

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context
        
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('product_list')

class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_delete.html'
    success_url = reverse_lazy('supplier_list')

class StockListView(ListView):
    model = Stock
    template_name = 'stocks/stock_list.html'
    context_object_name = 'stocks'

class StockDetailView(DetailView):
    model = Stock
    template_name = 'stocks/stock_detail.html'

class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stocks/stock_form.html'
    success_url = reverse_lazy('stock_list')

class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stocks/stock_form.html'
    success_url = reverse_lazy('stock_list')

class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'stocks/stock_delete.html'
    success_url = reverse_lazy('stock_list')

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients/ingredient_list.html'
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredients/ingredient_detail.html'

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredients/ingredient_form.html'
    success_url = reverse_lazy('ingredient_list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredients/ingredient_form.html'
    success_url = reverse_lazy('ingredient_list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredients/ingredient_delete.html'
    success_url = reverse_lazy('ingredient_list')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('main')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST) 
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next')) 
            return redirect('main')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    
    return render(request, 'auth/registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('main')