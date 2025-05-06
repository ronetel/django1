
from django.shortcuts import render, get_object_or_404, redirect 
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop_project.models import *
from .forms import *
from .bascket import Basket

@login_required
def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})
                  
def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id) 
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear (request):
    basket = Basket (request) 
    basket.clear()
    return redirect('basket_detail')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0: 
        return redirect('product')
    form = OrderForm(request.POST)
    if form.is_valid(): 
        order = Order.objects.create( 
            comment=form.cleaned_data['comment'], 
            delivery_adress=form.cleaned_data['delivery_adress'],
            delivery_type=form.cleaned_data['delivery_type']
         )
        order.price = basket.get_total_price() 
        for item in basket: 
            pos_order = ProductInCheck.objects.create( 
                product=item['product'], 
                count=item['count'], 
                order=order
            )
        basket.clear() 
    return redirect('basket_detail') 
@login_required
def open_order (request):
    context = {
        'form_order': OrderForm 
    }
    return render(request, 'order/order_form.html', context)