from django.shortcuts import render
from products.models import Product
from django.db.models import Q
from django.conf import settings
import os
from cart.cart import Cart
# Create your views here.

def index(request):

    qs = Product.objects.all()
    context = {"qs":qs}
    return render(request,'products/view.html', context)

def search(request):

    query = request.GET.get('q')
    object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))


    for a in object_list:
        name = a.name
        image = a.image
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # prod_image = settings.MEDIA_ROOT + image
    image = os.path.join(settings.MEDIA_ROOT, str(image))
    pic = str(image)
    context = {
        'object_list':object_list,
        # 'base_url': base_url,
        'image':image

    }
    return render(request,'products/view.html', context)

def add_to_cart(request, product_id, quantity):
    quantity = quantity
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)
    return render(request, 'unify/products/cart.html', {'cart': Cart(request)})

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return render(request, 'unify/products/cart.html', {'cart': Cart(request)})

def get_cart(request):
    return render(request, 'unify/products/cart.html', {'cart': Cart(request)})