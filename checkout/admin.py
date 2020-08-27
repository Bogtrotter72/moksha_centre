from django.contrib import admin
from .models import Order, OrderLineItem

# Allow line items to be added and edited in the order model


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Include the inline item in the order model
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('order_number', 'full_name', 'email',
              'street_address1', 'street_address2', 'town_or_city',
              'county', 'country', 'postcode', 'date', 'order_total')

    list_display = ('order_number', 'full_name', 'date', 'order_total')

    ordering = ('-date',)
