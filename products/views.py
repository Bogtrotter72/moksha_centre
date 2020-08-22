from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .models import CarouselImage, Product


def all_products(request):
    object_list = Product.objects.all()

    # limit products to 20 per page
    paginator = Paginator(object_list, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    carousel_images = CarouselImage.objects.filter(product__id=product_id)
    mens = False
    pants = False

    tags = product.tags.all()
    for tag in tags:
        if tag.name == 'mens':
            mens = True
        if tag.name == 'pants':
            pants = True

    context = {
        'carousel_images': carousel_images,
        'product': product,
        'tags': tags,
        'mens': mens,
        'pants': pants,
    }

    return render(request, 'products/product_detail.html', context)
