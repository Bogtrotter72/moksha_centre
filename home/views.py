from django.shortcuts import render
from products.models import Product

# Create your views here.


def home(request):
    products = Product.objects.all()

    offers = []
    recent_products = []

    for product in products:
        for tag in product.tags.all():
            if tag.name == 'recent':
                recent_products.append(product)
            elif tag.name == 'offer':
                offers.append(product)


    context = {
        'offers': offers,
        'recent_products': recent_products,
    }

    return render(request, 'home/index.html', context)
