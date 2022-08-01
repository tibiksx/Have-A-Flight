from django.contrib.auth.models import AbstractUser

from django.db import models
from .address import Address


class User(AbstractUser):
    address = models.ForeignKey(Address, on_delete=models.deletion.CASCADE, related_name='users', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    tel_no = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.username, self.first_name, self.last_name)
