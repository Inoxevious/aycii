from django.shortcuts import render
from django.db.models import Q
from django.conf import settings
import os
import mimetypes
from cart.cart import Cart
# Create your views here.
from django.views import generic

def index(request):

    return render(request,'unify/index.html')


def about(request):
    return render(request, 'unify/index.html')

def login(request):
    return render(request, 'unify/index.html')

def contact(request):
    return render(request, 'unify/index.html')

def blog_detail(request):
    return render(request, 'unify/index.html')

def product(request):
    return render(request, 'unify/index.html')

def product_detail(request):
    return render(request, 'unify/index.html')

def blog(request):
    return render(request, 'unify/bindex.html')

def cart(request):
    return render(request, 'unify/index.html')

def faq(request):
    return render(request, 'unify/index.html')