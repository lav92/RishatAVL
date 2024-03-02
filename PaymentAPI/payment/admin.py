from django.contrib import admin
from django.contrib.admin import register

from payment.models import Item, Order, Discount


@register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'get_total')


@register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('percent_off', 'duration')
