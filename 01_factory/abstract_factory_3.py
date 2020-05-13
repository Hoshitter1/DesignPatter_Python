from abc import ABC


class Factory:
    """object creation is delegated to this class"""

    def __init__(self, animal_class):
        self.animal = animal_class()

    def check_animal(self):
        self.animal.eat()
        self.animal.speak()


class Animal(ABC):
    """Template method"""

    def eat(self):
        pass

    def speak(self):
        pass


class Cow(Animal):

    def eat(self):
        print('cow eats grasses')

    def speak(self):
        print('moooooooooooooo')


class Chicken(Animal):

    def eat(self):
        print('checkin eats stuff')

    def speak(self):
        print('bbbbiiirrrrrrdd')


if __name__ == "__main__":
    cow_factory = Factory(Cow)
    cow_factory.check_animal()

    chiken_factroy = Factory(Chicken)
    chiken_factroy.check_animal()
