from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



class Item(models.Model):
    class Status(models.TextChoices):
        ZERO = 'N', 'Скоро на складе'
        NOT_ZERO = 'Y', 'В наличии'

    name = models.CharField(max_length=55, verbose_name='Название')
    slug = models.SlugField(max_length=55, verbose_name='Артикул', unique=True)
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ZERO, verbose_name='Статус')
    length = models.PositiveIntegerField(blank=True, null=True, verbose_name='Длина')
    weight = models.PositiveIntegerField(blank=True, null=True, verbose_name='Ширина')
    quantity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Колличество')
    price = models.DecimalField(default=1990, verbose_name='Цена', decimal_places=0, max_digits=8)
    publish = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return self.name

class ItemImages(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images/')
    is_main = models.BooleanField(default=False, verbose_name='Главная')
    is_active = models.BooleanField(default=True, verbose_name='Активная')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.item.name}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

@receiver(post_save, sender=ItemImages)
def set_main_image(sender, instance, **kwargs):
    if instance.is_main:
        # Устанавливаем is_main в False для всех других изображений связанных с этим товаром
        ItemImages.objects.filter(item=instance.item, is_main=True).exclude(id=instance.id).update(is_main=False)

