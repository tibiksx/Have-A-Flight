from django.shortcuts import render, redirect

from ..forms import UserForm, AddressForm
from ..models import User, Address


def register(request):
    if request.method == 'GET':
        form_user = UserForm()
        form_address = AddressForm()
        context = {
            'form_user': form_user,
            'form_address': form_address,
        }
        return render(request, 'register.html', context=context)

    elif request.method == 'POST':

        request_user_form = UserForm(request.POST)
        request_address_form = AddressForm(request.POST)
        if request_user_form.is_valid() and request_address_form.is_valid():
            address = Address.objects.create(
                country=request_address_form.cleaned_data['country'],
                city=request_address_form.cleaned_data['city'],
                line1=request_address_form.cleaned_data['line1'],
                line2=request_address_form.cleaned_data['line2'],
            )
            user = User.objects.create(
                username=request_user_form.cleaned_data['username'],
                first_name=request_user_form.cleaned_data['first_name'],
                last_name=request_user_form.cleaned_data['last_name'],
                email=request_user_form.cleaned_data['email'],
                address=address,
            )
            user.set_password(request_user_form.cleaned_data['password'])
            user.save()
        return redirect('/login')
