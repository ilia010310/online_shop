from django.contrib import admin
from order.models import Status, ItemsInOrder, Order


class ItemsInOrderInline(admin.TabularInline):
    model = ItemsInOrder
    extra = 0

# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'is_active', 'created', 'updated']
#     ordering = ['id']

@admin.register(ItemsInOrder)
class ItemsInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity', 'created', 'updated' ]
    ordering = ['id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'customer_name', 'customer_email', 'comments', 'status', 'created', 'updated' ]
    ordering = ['status']
    inlines = [ItemsInOrderInline]
