# del method 
class Car:
    def __init__(self):
        pass

c1 = Car()
print(c1)
del c1
print(Car())

# attribute ko del kerta ha
class Car:
    def __init__(self,name):
        self.name = name

c1 = Car("BMW")
print(c1.name)
del c1.name
# print(c1.name)


# private method kisi bhi method or attribute ko hum private ker sekta ha

class Bank:
    def __init__(self,bank_name,pin):
        self.bank_name = bank_name
        # private attribute
        # self.__pin = pin
        self.pin = pin
b1 = Bank("Alhabib",123)
# print(b1.bank_name,b1.__pin)
print(b1.bank_name,b1.pin)

# 2 example
class Car:
    def __init__(self,name):
        self.name = name
    def __info(self):
        print("hello my name is rabia and my pasword is secret")
# hum class ke ander is private method ko kisi or method mein add ker ke public kerwa sekta 
# ha like
    def behind(self):                      # public method
        self.__info() 
c1 = Car("BMW")
print(c1.name)
# c1.__info() error de ga beacause ya aik private ha
c1.behind()

# asa hum private method ko kisi or method mein call ker sekta ha 
# or wo public print ho gaye ga