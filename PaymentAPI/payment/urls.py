from django.urls import path

from payment.views import proceed_to_checkout, get_item, proceed_to_checkout_order

app_name = 'payment'

urlpatterns = [
    path('buy/<int:item_id>/', proceed_to_checkout, name='checkout'),
    path('item/<int:item_id>/', get_item, name='item'),
    path('order/<int:order_id>/', proceed_to_checkout_order, name='checkout_order'),
]
