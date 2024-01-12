from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddItemForm
from shop.models import Item, ItemImages


def items_list(request):
    # items = Item.objects.all()
    # return render(request,
    #               'shop/item/list.html',
    #               {'items': items})
    cart_item_form = CartAddItemForm()
    items_images = ItemImages.objects.filter(is_active=True, is_main=True)
    return render(request, 'shop/item/list.html',
                  {'items_images': items_images,
                           'cart_item_form': cart_item_form})


def item_detail(request, name):
    item = get_object_or_404(Item,
                             slug=name)
    cart_item_form = CartAddItemForm()
    images = ItemImages.objects.filter(item__slug=name)
    return render(request,
                  'shop/item/detail.html',
                  {'item': item,
                    'images': images,
                   'cart_item_form': cart_item_form})