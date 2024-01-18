from django.shortcuts import render
from cart.cart import Cart
from django.http import HttpResponse
from lameli import settings
from order.forms import OrderForm
from order.models import Order, ItemsInOrder
from shop.models import Item


def order(request):
    if not Cart(request):
        return render(request, 'empty_cart.html')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['total_price'] = Cart(request).get_total_price()

            final_order = Order(**form_data)

            final_order.save()
            for item in Cart(request):
                print(item)
                product = Item.objects.get(name=item['product'])
                quantity = item['quantity']
                price = item['price']
                # image = item['image']
                total_price = quantity * price
                final_item_in_order = {'quantity': quantity,
                                                    'price_per_item': price,
                                                    'order': final_order,
                                                    'item': product,
                                                    'total_price': total_price,
                                                    }
                one_item_in_total_order = ItemsInOrder(**final_item_in_order)
                one_item_in_total_order.save()

            name = form_data['customer_name']
            return render(request, 'solution.html', {'name': name})

    else:
        form = OrderForm()
        return render(request, 'order.html', {'form': form})
