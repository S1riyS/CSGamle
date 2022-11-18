from abc import ABCMeta, abstractmethod

from django.db import models

from csgamble.utils.models import get_hash_name


class ItemAbstractMeta(ABCMeta, type(models.Model)):
    pass


class ItemAbstract(models.Model, metaclass=ItemAbstractMeta):
    @property
    @abstractmethod
    def hash_name(self, *args, **kwargs):
        """Return hash name of item"""
        return 1

    @property
    def market_url(self):
        print(self.hash_name)
        return f'https://market.csgo.com/?search={self.hash_name}'

    @property
    def image_url(self, width: int = 300):
        return f'https://cdn.csgo.com//item/{self.hash_name}/{width}.png'

    class Meta:
        abstract = True
