from django.contrib import messages
from django.shortcuts import get_object_or_404, HttpResponse, redirect, render, reverse
from products.models import Product

# Create your views here.
def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:                                                                # If the item has a size
        if quantity > 0:                                                    # and the quantity is greater than 0
            bag[item_id]['items_by_size'][size] = quantity                  # get the specific size and set its quantity accordingly
        else:
            del bag[item_id]['items_by_size'][size]                         # or remove if quantity is zero
            if not bag[item_id]['items_by_size']:                           # If items by size is now empty
                bag.pop(item_id)                                            # remove the item entirely

    else:                                                                   # If there is no size
        if quantity > 0:                                                    # and the quantity is greater than 0
            bag[item_id] = quantity                                         # update the quantity
        else:
            bag.pop(item_id)                                                # remove the item entirely
    
    request.session['bag'] = bag                                            # place bag into the session
    return redirect(reverse('view_bag'))                                    # return to the shopping bag


def remove_from_bag(request, item_id):
    try:
        product = Product.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:                                                            # If the item has a size
            del bag[item_id]['items_by_size'][size]                         # remove the specific size key in the items_by_size dictionary
            if not bag[item_id]['items_by_size']:                           # If items by size is now empty
                bag.pop(item_id)                                                # remove the item entirely
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')

        else:                                                               # If there is no size
            bag.pop(item_id)                                                    # remove the item entirely
            messages.success(request, f'Removed {product.name} from your bag')
        
        request.session['bag'] = bag                                        # place bag into the session
        return HttpResponse(status=200)                                     # Send a Http 200 response to indicate successful removal of item

    except Exception as e:
        messages.error(request, f'Error removing item; {e}')
        return HttpResponse(status=500)