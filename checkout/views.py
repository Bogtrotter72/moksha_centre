from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Thers is nothing in your shopping bag at the moment!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)