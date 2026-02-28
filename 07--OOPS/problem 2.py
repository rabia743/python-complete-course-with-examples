class Animale():
    pass

class Pets(Animale):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

a = Dog()
a.bark()