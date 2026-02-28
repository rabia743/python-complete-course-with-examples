# abstraction se phela uska module or import kerna hoga
# because python naho samjha ga ke abstract method ia hota ha

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def info(self):
        pass

class B(A):
    def info(self):
        print("hello")

class C(A):
    def info(self):
        print("Rabia")

c = B()
c.info()
c = C()
c.info()
''' abstract method ka object creat nahi ho sekta ha because
its role '''


from abc import ABC, abstractmethod
class R(ABC):
    @abstractmethod
    def info(self):
        pass

class S(R):
    def info(self):
        print("hello")

class T(S):
    def info(self):
        super().info()
        print("Rabia")

U = T()
U.info()

# example 3
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def engine(self):
        pass

class Engine(ABC):
    def work(self):
        print("engine work like")

class User(Engine):
    def info(self):
        super().work()
        print("I am start the car")

# v = Engine()
# v.work()
B = User()
B.info()


from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def engine(self):
        pass

# class Engine(Car):
#     pass
# or ya error de raha ha
v = Engine()

