
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        "title": "HOME - главная",
        "content": "Магазин мебели HOME",
        "categories": categories
    }


    return render(request, "main/index.html", context)

def about(request):

    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Текст о том какой у нас классный и хороший товар"
    }

    return render(request, "main/about.html", context)