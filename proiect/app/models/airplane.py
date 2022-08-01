from django.db import models


class Airplane(models.Model):
    registration_no = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    model_no = models.CharField(max_length=255)
    airline = models.CharField(max_length=255)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.airline, self.model_no, self.capacity, self.registration_no)
