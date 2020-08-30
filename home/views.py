from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render, reverse
from products.models import Product

from .forms import EmailContactForm


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

    bg_img = True
    home = True

    sent = False

    # Form submitted
    if request.method == 'POST':
        form = EmailContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']}, sent the following message:"
            message = f"{cd['message']}"
            send_mail(subject, message, '2ciaran7@gmail.com',['2ciaran7@gmail.com'], fail_silently=True)
            sent = True
            messages.success(request, 'Your email was sent successfully. Our team will respond within 24 hrs.')
            return redirect(reverse('home'))

    else:
        form = EmailContactForm()


    context = {
        "bg_img": bg_img,
        "form": form,
        "home": home,
        'offers': offers,
        'recent_products': recent_products,
    }

    return render(request, 'home/index.html', context)
