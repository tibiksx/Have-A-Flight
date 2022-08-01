from django.db import models

from .user import User
from .card import Card
import datetime


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE, related_name='transactions')
    card = models.ForeignKey(Card, on_delete=models.deletion.CASCADE, related_name='transactions')
    date_and_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return '{}, {}'.format(self.user, self.card)
