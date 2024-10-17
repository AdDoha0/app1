from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "title": "Home",
        "content": "Главная страница HOME"
    }
    return render(request, "main/index.html", data)

def about(request):
    return HttpResponse("about page")