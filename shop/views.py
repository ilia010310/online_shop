from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddItemForm
from shop.models import Item, ItemImages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def items_list(request):
    cart_item_form = CartAddItemForm()
    items_images = ItemImages.objects.filter(is_active=True, is_main=True)
    paginator = Paginator(items_images, 12)
    page_number = request.GET.get('page', 1)
    try:
        images = paginator.page(page_number)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'shop/item/list.html',
                  {'items_images': images,
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