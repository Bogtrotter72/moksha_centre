from django.contrib import admin
from .models import CarouselImage, Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'sku',
                    'tag_list', 'has_sizes', 'price', 'rating')
    search_fields = ('name', 'manufacturer')
    ordering = ('name', 'manufacturer')

    # Show the product tags
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('product_sku', 'image_url')

    def product_sku(self, obj):
        return obj.product.sku
