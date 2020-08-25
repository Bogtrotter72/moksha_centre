from django.urls import path
from .views import add_to_bag, adjust_bag, remove_from_bag, view_bag

urlpatterns = [
    path('', view_bag, name="view_bag"),
    path('add/<item_id>', add_to_bag, name="add_to_bag"),
    path('adjust/<item_id>/', adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', remove_from_bag, name='remove_from_bag'),
]
