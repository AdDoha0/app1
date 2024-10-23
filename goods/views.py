
from turtle import title
from django.shortcuts import render
from django.template import context

from goods.models import Products



def catalog(request):

    goods =  Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods
    }

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product
    }

    return render(request, 'goods/product.html', context)