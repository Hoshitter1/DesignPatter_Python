from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


class IDCard(Product):
    def __init__(self, owner):
        self.owner = owner

    def use(self):
        print(f"Use {self.owner}'s card")


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.owners.append(product.owner)


if __name__ == '__main__':
    factory = IDCardFactory()
    card1 = factory.create('Hoshito')
    card2 = factory.create('Hoge')
    card1.use()
    card2.use()
