from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from ..forms import PassengerForm, TicketForm, FlightForm
from ..models import Passenger, Ticket, Flight, Transaction, Card
import datetime

def render_buy_ticket(request, errors):
    user = request.user
    flight_form = FlightForm(initial = {'id': request.GET.get('flight')})
    passenger_form = PassengerForm()
    ticket_form = TicketForm()
    cards = user.cards.all()
    return render(request, 'ticket.html', {'passenger_form': passenger_form, 'ticket_form': ticket_form, 'flight_form': flight_form, 'cards': cards, 'user': user, 'errors': errors})



@login_required
def ticket(request):
    if request.method == 'POST':
        request_passenger_form = PassengerForm(request.POST)
        request_ticket_form = TicketForm(request.POST)
        flight_id = request.POST.get('flight')
        flight = Flight.objects.get(id=flight_id)
        if request_passenger_form.is_valid() and request_ticket_form.is_valid():

            has_flight_seat_combination = Ticket.objects.filter(flight=flight, seat = request_ticket_form.cleaned_data['seat']).count() != 0
            if has_flight_seat_combination:
                return render_buy_ticket(request, errors=["The seat is already taken! Please choose another seat!"])

            passenger = Passenger.objects.create(
                name=request_passenger_form.cleaned_data['name'],
                date_of_birth=request_passenger_form.cleaned_data['date_of_birth'],
                tel_no=request_passenger_form.cleaned_data['tel_no'],
            )
            transaction = Transaction.objects.create(
                user=request.user,
                card=Card.objects.filter(card_no=request.POST.get('card')).first()
            )
            ticket = Ticket.objects.create(
                passenger=passenger,
                seat=request_ticket_form.cleaned_data['seat'],
                flight=flight,
                transaction=transaction,
                flightid=flight_id
            )

        return redirect('/home')
    elif request.method == 'GET':
        return render_buy_ticket(request, errors=[])

