from django.db import models


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

    def __str__(self):
        return self.name


class Item(models.Model):
    weapon = models.ForeignKey('Weapon', on_delete=models.PROTECT, null=False)
    skin_name = models.CharField(max_length=50)
    wear_level = models.ForeignKey('WearLevel', on_delete=models.PROTECT, null=False)
    rarity = models.ForeignKey('Rarity', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.weapon.name} | {self.skin_name} ({self.wear_level.name})'
