from django.db import models

from csgamble.apps.core.models import Item


class Case(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=False, default=1000)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.name.upper()} КЕЙС'
