from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.


def regester(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name
        )

        user.save()
        print('User Created')
        return redirect('/OrderOnline/')
    else:
        return render(request, 'regester.html')
