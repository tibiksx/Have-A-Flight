from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.shortcuts import redirect, HttpResponse, render


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            django_login(request, user)
            return redirect('/home')
        else:
            return HttpResponse('Invalid user try again!')
    else:
        return render(request, 'login.html')
