from django.db import models

from ..models import User


class Card(models.Model):
    name = models.CharField(max_length=255)
    card_no = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE, related_name='cards')

    def __str__(self):
        return '{}'.format(self.card_no)
