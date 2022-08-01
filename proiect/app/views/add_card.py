from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import CardForm
from ..models import Card


@login_required
def add_card(request):
    if request.method == 'POST':
        request_card_form = CardForm(request.POST)
        if request_card_form.is_valid():
            card = Card.objects.create(
                name=request_card_form.cleaned_data['name'],
                card_no=request_card_form.cleaned_data['card_no'],
                exp_month=request_card_form.cleaned_data['exp_month'],
                exp_year=request_card_form.cleaned_data['exp_year'],
                user=request.user
            )
        return redirect('/home')
    elif request.method == 'GET':
        form_card = CardForm()
        context = {
            'form_card': form_card
        }
        return render(request, 'card.html', context=context)
