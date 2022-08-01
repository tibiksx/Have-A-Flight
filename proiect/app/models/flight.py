from django.db import models

from .airplane import Airplane
from .airport import Airport


class Flight(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.deletion.CASCADE, related_name='flights')
    departure = models.DateTimeField()
    available_seats = models.PositiveIntegerField()
    destination = models.ForeignKey(Airport, on_delete=models.deletion.CASCADE, related_name='destination_flights')
    source = models.ForeignKey(Airport, on_delete=models.deletion.CASCADE, related_name='source_flights')
    price = models.FloatField()
    currency = models.CharField(max_length=20)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.departure, self.source, self.destination, self.airplane, self.price, self.currency, self.available_seats)
