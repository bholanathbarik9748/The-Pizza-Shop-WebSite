from django.shortcuts import render
from .models import item

# Create your views here.


def home(request):
    return render(request, 'home.html')


def OrderOnline(request):
    res = item.objects.all()
    return render(request, 'OrderOnline.html', {'i': res})
