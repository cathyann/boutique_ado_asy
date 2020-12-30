from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I421HGT7YR31uXW18rYSk05UktEv8IgC8SkFuSNIlM2A4xOWcI37h40X6py1HjpAyY4EqrxDBW4pEPWvt3eINg700wa4z7BO9',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
