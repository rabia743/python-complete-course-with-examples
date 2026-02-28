class A:
    def __init__(self,age):
        self.__age = age
    @property
    def age(self):
        return self.__age

s = A(21)
print(s.age)

# two types of getter and setter
class Z:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative")
        else:
            self.__age = value

c = Z(21)
print(c.age)
c.age = 22
print(c.age)