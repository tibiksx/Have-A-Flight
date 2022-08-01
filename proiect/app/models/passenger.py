from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    tel_no = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.name)
