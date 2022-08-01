from django.contrib import admin

from .models.user import User
from .models.passenger import Passenger
from .models.airplane import Airplane
from .models.flight import Flight
from .models.transaction import Transaction
from .models.ticket import Ticket
from .models.card import Card
from .models.airport import Airport
from .models.address import Address

# Register your models here.

admin.site.register(User)
admin.site.register(Passenger)
admin.site.register(Airplane)
admin.site.register(Flight)
admin.site.register(Transaction)
admin.site.register(Ticket)
admin.site.register(Card)
admin.site.register(Airport)
admin.site.register(Address)
