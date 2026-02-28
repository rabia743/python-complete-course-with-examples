# the function inside the class is called method
class Student:
    def __init__(self, name):
        self.name = name

    def info(self):   # <-- method inside class
        print(f"The student and his name is {self.name}")

s1 = Student("rabia")
s1.info()


# example no 2
class Car:
    def __init__(self, name,brand,year):
        self.name = name
        self.brand = brand
        self.year = year

    def info(self):   # <-- method inside class
        print(f"my car and his name is {self.name},and his brand {self.brand} year is {self.year}")
    def collection(self):
        print("this is my new car and this car is added in my car collection")

c1 = Car("My car","BMW",2024)
c1.info()
c1.collection()

