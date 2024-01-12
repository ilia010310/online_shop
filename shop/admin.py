from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Item, ItemImages

class ItemImageInline(admin.TabularInline):
    model = ItemImages
    extra = 3

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'name', 'slug', 'status', 'price']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name',]
    ordering = ['-publish']
    inlines = [ItemImageInline]

    def image_show(self, obj):
        if obj.images.get(is_main=True):
            if obj.images.get(is_main=True):
                return mark_safe("<img src='{}' width='60' />".format(obj.images.get(is_main=True).image.url))
            return "None"

    image_show.__name__ = "Картинка"



# @admin.register(ItemImages)
# class ItemImageAdmin(admin.ModelAdmin):
#     list_display = ['image_show', 'item', 'is_active', 'created', 'updated']
#     ordering = ['-updated']
#
#     def image_show(self, obj):
#         if obj.image:
#             if obj.image:
#                 return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
#             return "None"
#
#     image_show.__name__ = "Картинка"



    

