import stripe
from django.shortcuts import render, redirect

from payment.models import Item, Order
import config

stripe.api_key = config.STRIPE_API_KEY


def proceed_to_checkout(request, item_id):
    item = Item.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )

    return redirect(session.url, code=303)


def proceed_to_checkout_order(request, order_id):
    order = Order.orders.get(pk=order_id)
    if order.discount:
        coupon = stripe.Coupon.create(
            duration=order.discount.duration,
            percent_off=order.discount.percent_off,
        )

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': f'order {order_id}'
                },
                'unit_amount': int(order.get_total.get('price__sum') * 100),
            },
            'quantity': 1,
        }],
        discounts=[{'coupon': coupon.id}] if order.discount else None,
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )

    return redirect(session.url, code=303)


def get_item(request, item_id):
    pk = item_id
    item = Item.objects.get(pk=pk)
    return render(request, 'payment/item_details.html', {'item': item})
