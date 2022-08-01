from django.db import models

from .address import Address


class Airport(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.code, self.name, self.city, self.country)
