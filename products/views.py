from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import CarouselImage, Product


def all_products(request):
    object_list = Product.objects.all()
    filtered = False
    filtered_list = []
    query = None
    tag = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter a search term!")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        object_list = object_list.filter(queries)

    if 'tag' in request.GET:
        tags = request.GET['tag'].split(',')
        tags.sort()


        for product in object_list:
            product_tags = []
            for tag in product.tags.all():
                product_tags.append(tag.name)
            product_tags.sort()
            if tags == product_tags:
                filtered_list.append(product)
                product_tags = []

        filtered = True
        object_list = filtered_list
    
    products_returned = len(object_list)

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
        'filtered': filtered,
        'page': page,
        'products': products,
        'returned': products_returned,
        'search_term': query,
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
