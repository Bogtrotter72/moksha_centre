from django.contrib import messages
from django.shortcuts import get_object_or_404, HttpResponse, redirect, render, reverse
from products.models import Product

# Create your views here.


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]["items_by_size"].keys():
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request, f'Updated {product.name.lower()}, size {size.upper()} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request, f'Added {product.name.lower()}, size {size.upper()}, quantity {bag[item_id]["items_by_size"][size]} to your bag')
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request, f'Added {product.name.lower()}, size {size.upper()} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name.lower()} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name.lower()} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:                                                                # If the item has a size
        if quantity > 0:                                                    # and the quantity is greater than 0
            # get the specific size and set its quantity accordingly
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                request, f'Updated {product.name.lower()}, size {size.upper()} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            # or remove if quantity is zero
            del bag[item_id]["items_by_size"][size]
            # If items by size is now empty
            if not bag[item_id]["items_by_size"]:
                # remove the item entirely
                bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name.lower()}, size {size.upper()} from your bag')

    else:                                                                   # If there is no size
        if quantity > 0:                                                    # and the quantity is greater than 0
            # update the quantity
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name.lower()} quantity to {bag[item_id]}')
        else:
            # remove the item entirely
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name.lower()} from your bag')

    # place bag into the session
    request.session['bag'] = bag
    # return to the shopping bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:                                                            # If the item has a size
            # remove the specific size key in the items_by_size dictionary
            del bag[item_id]["items_by_size"][size]
            # If items by size is now empty
            if not bag[item_id]["items_by_size"]:
                # remove the item entirely
                bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name.lower()}, size {size.upper()} from your bag')

        else:                                                               # If there is no size
            # remove the item entirely
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name.lower()} from your bag')

        # place bag into the session
        request.session['bag'] = bag
        # Send a Http 200 response to indicate successful removal of item
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item; {e}')
        return HttpResponse(status=500)
