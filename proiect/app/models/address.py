from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    line1 = models.CharField(max_length=50, null=True, blank=True)
    line2 = models.CharField(max_length=50, null=True, blank=True)
    optional = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.line1, self.city, self.country)
