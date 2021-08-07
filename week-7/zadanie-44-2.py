from dataclasses import dataclass


@dataclass()  # @datacless ma domyślnie zdefiniowane __repe__ co pozwala na wyświetlanie printa
class Item:
    name: str
    price: float
    discount: float


class Collection:
    def __init__(self):
        self.items = []

    @classmethod
    def create_with_items(cls, *args):
        collections = cls()
        collections.items.extend(args)

        return collections

it = Item('chleb', 4, 0.1)

i2 = Item('mleko', 2.3, 0)

col = Collection.create_with_items(it,i2)

print(col.items)

