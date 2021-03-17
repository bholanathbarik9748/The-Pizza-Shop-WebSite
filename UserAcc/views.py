from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def regester(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User-Name Already Available...')
                print("User-Name Already Available...")
                return redirect('/UserAcc/regester/')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Id Already Available...')
                print("Email Id Already Available...")
                return redirect('/UserAcc/regester/')

            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name
                )
            user.save()
            print('User Created')
            return redirect('/OrderOnline/')
        else:
            messages.info(request, 'Password not match !!!!')
            print("Password not match !!!!")
            return redirect('/UserAcc/regester/')
    else:
        return render(request, 'regester.html')


def loginAcc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/OrderOnline/')
        else:
            messages.info(request, 'User not Available...!!!!')
            return redirect('/UserAcc/loginAcc/')
    else:
        return render(request, 'loginAcc.html')
