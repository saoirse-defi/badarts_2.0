""" Django views for bag object. """
from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the user's shopping bag. """

    return render(request, 'bag/bag.html')


#@login_required()
def add_to_bag(request, product_id):
    """ Add quantity of specified item to the user's shopping bag. """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['items_by_size'].keys():
                bag[product_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 f'Added {product.name} {size}g '
                                 'to your shopping bag')
            else:
                bag[product_id]['items_by_size'][size] = quantity
                messages.add_message(request, 60,
                                     f'Added {product.name} {size}g '
                                     'to your shopping bag')
        else:
            bag[product_id] = {'items_by_size': {size: quantity}}
            messages.add_message(request, 60, f'Added {product.name} {size}g '
                                 'to your shopping bag')
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
            messages.add_message(request, 60,
                                 f'Updated the quantity of {product.name}')
        else:
            bag[product_id] = quantity
            messages.add_message(request, 60, f'Added {product.name} {size}g '
                                 'to your shopping bag')

    request.session['bag'] = bag

    return render(request, 'bag/bag.html')


def adjust_bag(request, product_id):
    """ Add quantity of specified item to the user's shopping bag. """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[product_id]["items_by_size"][size] = quantity
            messages.add_message(request, 60,
                                 f'Updated {product.name} '
                                 f'quantity to '
                                 f'{bag[product_id]["items_by_size"][size]}')
        else:
            del bag[product_id]["items_by_size"][size]
            if not bag[product_id]["items_by_size"]:
                bag.pop(product_id)
            messages.info(request,
                          f'Removed {product.name} from your shopping bag')
    else:
        if quantity > 0:
            bag[product_id] = quantity
            messages.add_message(request, 60,
                                 f'Updated {product.name} '
                                 f'quantity to {bag[product_id]}')
        else:
            bag.pop[product_id]
            messages.add_message(request, 60,
                                 f'Removed {product.name} '
                                 'from your shopping bag')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, product_id):
    """ Add quantity of specified item to the user's shopping bag. """
    try:
        product = get_object_or_404(Product, pk=product_id)
        size = None

        if 'product_size' in request.POST:
            size = request.POST['product_size']

        bag = request.session.get('bag', {})

        if size:
            del bag[product_id]['items_by_size'][size]
            if not bag[product_id]['items_by_size']:
                bag.pop(product_id)
            messages.add_message(request, 60,
                                 f'Removed {product.name} {size}g '
                                 'from your shopping bag')

        else:
            bag.pop(product_id)
            messages.add_message(request, 60,
                                 f'Removed {product.name} '
                                 'from your shopping bag')
        request.session['bag'] = bag

        HttpResponse(status=200)

        return redirect(reverse('view_bag'))
    except Exception:
        return HttpResponse(status=500)