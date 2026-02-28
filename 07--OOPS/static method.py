# ststic method mein humeha function ke parameters mein koi self likna ki need nahi ha
# ya hum thub kerta ha jub humeha just simple funtion banana ho

class Car:
    def __init__(self, name,brand,year):
        self.name = name
        self.brand = brand
        self.year = year

    def info(self):   # <-- method inside class
        print(f"my car and his name is {self.name},and his brand {self.brand} year is {self.year}")    # 
# ya aik simple function ha is mein humeha kisi object ki need nahi ha isliya hum na 
# @staticmethod ka use ker ke self nahi lika or na hi error aya 
    @staticmethod
    def collection():
        print("this is my new car and this car is added in my car collection")

c1 = Car("My car","BMW",2024)
c1.info()
c1.collection()

''' class method ka use kerga ga jub hum instance attribute ki 
replace mein class attribute ko print kerwna chata ho '''

class Rabia:
    a = "rabia"
    def __init__(self,name):
        self.name = name
    @classmethod
    def show_a(cls):
        print(cls.a)
    def full(self):
        print(f"my name is {self.name}")
r = Rabia("zafar")
r.show_a()
