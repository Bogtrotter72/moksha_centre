from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'sku',
                    'tag_list', 'price', 'rating')
    search_fields = ('name', 'manufacturer')
    ordering = ('name', 'manufacturer')

    # Show the product tags
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
