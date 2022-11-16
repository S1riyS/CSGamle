from django.contrib import admin

from .models import Weapon, WearLevel, Rarity, Item


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class WearLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class RarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'weapon', 'skin_name', 'wear_level', 'rarity')


admin.site.register(Weapon, WeaponAdmin)
admin.site.register(WearLevel, WearLevelAdmin)
admin.site.register(Rarity, RarityAdmin)
admin.site.register(Item, ItemAdmin)
