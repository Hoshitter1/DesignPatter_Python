"""
One of the examples of how tob implement abstract_factory
"""

from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('this tea is amazing')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is so good')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(
            'put tea bag and pour some hot water'
            f'{amount}ml'
        )
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(
            'grind coffee beans and put a filter and etc'
            f'{amount}ml'
        )
        return Coffee()


def make_drink(type_):
    if type_ == 'tea':
        return TeaFactory().prepare(100)
    elif type_ == 'coffee':
        return CoffeeFactory().prepare(200)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        TEA = auto()
        COFFEE = auto()

    factories = []
    initialized = False

    def __init__(self):
        if self.initialized:
            return
        self.initialized = True
        for d in self.AvailableDrink:
            name = d.name[0] + d.name[1:].lower()
            factory_name = name + 'Factory'
            factory_instance = eval(factory_name)()
            self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
        drink_type = input(f'please pick drink 0-{len(self.factories) - 1}')
        idx = int(drink_type)
        amount_ = input('specify amount:')
        amount = int(amount_)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
