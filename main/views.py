from email import contentmanager
import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "title": "HOME - главная",
        "content": "Магазин мебели HOME",
    }


    return render(request, "main/index.html", context)

def about(request):

    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Текст о том какой у нас классный и хороший товар"
    }

    return render(request, "main/about.html", context)