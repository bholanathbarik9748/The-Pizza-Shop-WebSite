from django.shortcuts import redirect, render
from .models import item, ANTIPASTO, BURGUR, SAMOSA
from django.contrib.auth.models import User, auth

# Create your views here.


def home(request):
    return render(request, 'home.html')


def OrderOnline(request):
    res = item.objects.all()
    ant = ANTIPASTO.objects.all()
    bur = BURGUR.objects.all()
    sam = SAMOSA.objects.all()
    return render(request, 'OrderOnline.html', {'i': res, 'a': ant, 'b': bur, 's': sam})


def creteAcc(request):

    if request.method == 'POST':
        first_name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']

        user = User.objects.create_user(
            first_name=first_name, Last_Name=Last_Name, email=email, psw=psw, psw_repeat=psw_repeat)
        user.save()

        print('User Created')
        return redirect('')
    else:
        return render(request, 'creteAcc.html')


def loginAcc(request):
    return render(request, 'loginAcc.html')


def payment(request):
    return render(request, 'payment.html')


def cp(request):
    return render(request, 'cp.html')


def menu(request):
    res = item.objects.all()
    ant = ANTIPASTO.objects.all()
    bur = BURGUR.objects.all()
    sam = SAMOSA.objects.all()
    return render(request, 'menu.html', {'i': res, 'a': ant, 'b': bur, 's': sam})
