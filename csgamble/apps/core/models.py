import typing as t

from django.db import models

from csgamble.utils.models import get_hash_name
from .mixins import ItemAbstract


class Weapon(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class WearLevel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rarity(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=1, null=False)

    def __str__(self):
        return self.name


class Item(ItemAbstract):
    weapon = models.ForeignKey('Weapon', on_delete=models.PROTECT, null=False)
    skin_name = models.CharField(max_length=50)
    rarity = models.ForeignKey('Rarity', on_delete=models.PROTECT, null=False)

    @property
    def hash_name(self):
        return get_hash_name(item=self)

    def __str__(self):
        return f'{self.weapon.name} | {self.skin_name}'
