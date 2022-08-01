from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
import datetime

from ..models.flight import Flight
from ..models.airport import Airport
from ..models.ticket import Ticket


# def buy(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#

@login_required
def home(request):
    if request.user.is_authenticated:
        airports = Airport.objects.all()

        # if request.method == 'GET':
        #     flight = Flight.object.filter(id=int(request.GET.get('flight', None).first()))
        #     return render(request, 'ticket.html', {'flight': flight})

        if request.method == 'POST':
            print(request.__dict__)
            source = Airport.objects.filter(name=request.POST.get('source')).first()
            destination = Airport.objects.filter(name=request.POST.get('destination')).first()
            print(source)
            print(type(destination))
            date = request.POST.get('departure')
            print(date)
            date = date.replace('T', ' ')
            print(date)
            departure = datetime.datetime.strptime(date, '%Y-%m-%d')
            user = request.user
            print(type(departure))
            flights = Flight.objects.filter(destination=destination, source=source, departure__date=departure)
            transactions = user.transactions.all()
            print(flights)
            return render(request, 'home.html', {'airports': airports, 'flights': flights, 'transactions': transactions})
        elif request.method == 'GET':
            user = request.user
            transactions = user.transactions.all()
            flightst = Flight.objects.all()
            print(request.__dict__)
            return render(request, 'home.html', {'airports': airports, 'user': user, 'transactions': transactions, 'flightst': flightst})
        else:
            return HttpResponse('Not Logged In!')
