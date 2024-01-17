from django.shortcuts import render
from cart.cart import Cart
from django.http import HttpResponse
from lameli import settings
from order.forms import OrderForm
from order.models import Order


def order(request):
    if not Cart(request):
        return render(request, 'empty_cart.html')
    if request.method == 'POST':
        new_order = Order()
        form = OrderForm(request.POST)
        new_order.save()
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['total_price'] = Cart(request).get_total_price()
            print(form_data)
            final_order = Order(**form_data)
            final_order.save()
            return HttpResponse('<h1>Это успех</h1>')


    form = OrderForm()
    return render(request, 'order.html', {'form': form})
