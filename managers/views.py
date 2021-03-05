from django.shortcuts import render
from .models import item

# Create your views here.


def home(request):
    return render(request, 'home.html')


def OrderOnline(request):
    i = item()
    i.name = 'pizza1'
    i.price = 12
    return render(request, 'OrderOnline.html', {'i': i})
