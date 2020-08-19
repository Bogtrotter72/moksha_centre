from django.shortcuts import get_object_or_404, render
from .models import CarouselImage, Product

# Create your views here.


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    carousel_images = CarouselImage.objects.filter(product__id=product_id)

    context = {
        'product': product,
        'carousel_images': carousel_images,
    }

    return render(request, 'products/product_detail.html', context)
