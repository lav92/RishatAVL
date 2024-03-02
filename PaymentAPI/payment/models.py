from django.db import models
from django.db.models import Sum


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ManyToManyField('Order', related_name='items')

    def __str__(self):
        return self.name

    objects = models.Manager()


class Order(models.Model):
    discount = models.ForeignKey('Discount', null=True, on_delete=models.SET_NULL, related_name='orders', blank=True)

    orders = models.Manager()

    @property
    def get_total(self):
        return self.items.aggregate(Sum('price'))

    def __str__(self):
        return f'order #{self.pk}'


class Discount(models.Model):
    percent_off = models.IntegerField()
    duration = models.CharField(max_length=10) #One of forever, once, and repeating

    discounts = models.Manager()

    def __str__(self):
        return f'{self.percent_off} - {self.duration}'
