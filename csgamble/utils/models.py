import urllib
import typing as t

if t.TYPE_CHECKING:
    from csgamble.apps.core.models import Item, WearLevel

HashName = str


def get_hash_name(item: "Item", wear_level: t.Optional["WearLevel"] = None) -> HashName:
    DEFAULT_WEAR_LEVEL = 'Factory new'

    if wear_level is not None:
        concatenated_string = f'{item.weapon.name} | {item.skin_name} ({wear_level.name})'
    else:
        concatenated_string = f'{item.weapon.name} | {item.skin_name} ({DEFAULT_WEAR_LEVEL})'

    return urllib.parse.quote(concatenated_string)
