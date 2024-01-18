from django.shortcuts import render
from cart.cart import Cart
from django.http import HttpResponse
from lameli import settings
from order.forms import OrderForm
from order.models import Order, ItemsInOrder
from shop.models import Item
from django.core.mail import send_mail


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
            items_in_answer = 'Товары: \n\n'
            for item in Cart(request):

                product = Item.objects.get(name=item['product'])
                quantity = item['quantity']
                price = item['price']
                total_price = quantity * price
                items_in_answer += (f'{product.name}\nКоличество: {quantity} шт.\n'
                                    f'Цена за штуку: {price} руб. \n\n ')
                final_item_in_order = {'quantity': quantity,
                                                    'price_per_item': price,
                                                    'order': final_order,
                                                    'item': product,
                                                    'total_price': total_price,
                                                    }
                one_item_in_total_order = ItemsInOrder(**final_item_in_order)
                one_item_in_total_order.save()

            name = form_data['customer_name']

            subject = f"{name}, спасибо за заказ!"
            message = f"Ваш заказ уже принят в обработку.\n\n" \
                      f"Скоро с Вами свяжется наш менеджер."
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [form_data['customer_email']])

            subject = f"Новый заказ!"

            message = f"Имя покупателя: {name}.\n\n" \
                      f"Email: {form_data['customer_email']}\n\n" \
                      f'Телефон: {form_data["customer_phone"]}\n\n' \
                      f'ИНН: {form_data["customer_inn"]}\n\n' \
                      f'Комментарий: {form_data["comments"]}\n\n' \
                      f'{items_in_answer}\n\n' \
                      f'Итого: {form_data["total_price"]} руб.'
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      ['theilyaboyarintsev@gmail.com'])
            print(form_data)
            print(Cart(request))
            return render(request, 'solution.html', {'name': name})

    else:
        form = OrderForm()
        return render(request, 'order.html', {'form': form})
