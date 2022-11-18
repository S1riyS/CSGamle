from django.db import models

from csgamble.apps.core.models import Item, WearLevel
from csgamble.apps.core.mixins import ItemAbstract
from csgamble.utils.models import get_hash_name


class Case(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=False, default=1000)
    items = models.ManyToManyField(Item, through="CaseItem")

    def __str__(self):
        return f'{self.name.upper()} КЕЙС'


class CaseItem(ItemAbstract):
    case = models.ForeignKey(Case, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    wear_level = models.ForeignKey(WearLevel, on_delete=models.PROTECT, null=False)

    @property
    def hash_name(self, *args, **kwargs):
        return get_hash_name(item=self.item, wear_level=self.wear_level)

    def __str__(self):
        return f'{str(self.item)} ({str(self.wear_level)})'
