from django.shortcuts import render
from cart.cart import Cart


def order(request):


    return render(request, 'order.html')
