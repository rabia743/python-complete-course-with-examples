# encapsulaion hide the personal informaion on public
class A:
    def __init__(self,name,password):
        self.name = name
        self.__password = password

c = A("sania",123)
print(c.name)
# print(c.__password)

# example 2
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