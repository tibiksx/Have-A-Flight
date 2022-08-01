from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect


def logout(request):
    django_logout(request)
    return redirect('/login')
