from django.shortcuts import render
from cart.cart import Cart
from django.http import HttpResponse
from lameli import settings
from order.forms import OrderForm


def order(request):
    if not Cart(request):
        return render(request, 'empty_cart.html')

    # for example!
    print(Cart(request))
    form = OrderForm()
    return render(request, 'order.html', {'form': form})
