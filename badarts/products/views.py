from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .filters import ProductFilter
from .models import Product, Category
from .forms import ProductForm
from profile.models import UserProfile

# Custom Decorators


def superuser_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry only store owners can do that.')
            return redirect(reverse('error_handler_500'))
        else:
            return func(request)
    return wrapper


# Product Views

def all_products(request):
    """ A view to handle all products """

    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs

    if request.user.is_authenticated:
        current_user = UserProfile.objects.get(user=request.user)
        current_wishlist = Wishlist.objects.all().filter(user=current_user)

        context = {
            'products': products,
            'product_filter': product_filter,
            'current_wishlist': current_wishlist,
            'current_user': current_user,
        }

        return render(request, 'products/products.html', context)
    else:
        context = {
            'products': products,
            'product_filter': product_filter,
        }

        return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    wishlist_id = None

    try:
        current_user = UserProfile.objects.get(user=request.user)
    except Exception as e:
        current_user = None
        print(e)

    product = get_object_or_404(Product, pk=product_id)
    store = get_object_or_404(Store, pk=product.seller_store.store_id)

    if current_user is not None:
        try:
            current_wishlist = Wishlist.objects.all().filter(user=current_user)
            for wish in current_wishlist:
                if wish.product == product:
                    wishlist_id = wish.wishlist_id
        except Exception as e:
            wishlist_id = None
            print(e)

        if store.user == current_user:
            context = {
                'wishlist_id': wishlist_id,
                'current_user': current_user,
                'product': product,
                'store': store,
                }
            return render(request, 'products/product_detail.html', context)
        else:
            context = {
                'wishlist_id': wishlist_id,
                'current_user': current_user,
                'product': product,
                'store': store,
                }
            return render(request,
                          'products/product_detail_anon.html',
                          context)
    else:
        context = {
            'product': product,
            'store': store,
            }
        return render(request, 'products/product_detail_anon.html', context)
