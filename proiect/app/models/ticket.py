from django.db import models

from .flight import Flight
from .transaction import Transaction
from .passenger import Passenger


class Ticket(models.Model):
    class Meta:
        unique_together = (('flight', 'seat'), )
    flight = models.ForeignKey(Flight, on_delete=models.deletion.CASCADE, related_name='tickets')
    flightid = models.IntegerField()
    transaction = models.ForeignKey(Transaction, on_delete=models.deletion.CASCADE, related_name='tickets', null=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.deletion.CASCADE, related_name='tickets')
    seat = models.CharField(max_length=5)

    def __str__(self):
        return '{}, {}, {}'.format(self.flight, self.passenger, self.seat)
