from django.db import models
from django.db.models.signals import post_save

from shop.models import Item


class Status(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True, default='Новый')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=0,
                                      default=0, blank=True, null=True,
                                      verbose_name='Общая стоимость')
    customer_name = models.CharField(max_length=80)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=12)
    customer_inn = models.CharField(max_length=12, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ №{self.id} от {self.customer_name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ItemsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders',
                              verbose_name='Заказ №')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=0, default=0,
                                         verbose_name='Цена за штуку')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0,
                                      verbose_name='Общая стоимость')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.item.price
        self.price_per_item = price_per_item
        self.total_price = self.quantity * price_per_item

        super(ItemsInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ItemsInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ItemsInOrder)

