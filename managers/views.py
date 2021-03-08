from django.shortcuts import render
from .models import item, ANTIPASTO, BURGUR, SAMOSA

# Create your views here.


def home(request):
    return render(request, 'home.html')


def OrderOnline(request):
    res = item.objects.all()
    ant = ANTIPASTO.objects.all()
    bur = BURGUR.objects.all()
    sam = SAMOSA.objects.all()
    return render(request, 'OrderOnline.html', {'i': res, 'a': ant, 'b': bur, 's': sam})
