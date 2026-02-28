# there are four pillar of oop
# the first oop pillar discuss is inheritence
# the first type is basic inheritencs
class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
class Animale(Dog):
    def infor(self):
        print(f"Dog is animale name is {self.name} color is {self.color}")

d1 = Animale("jemmy","black")
d1.infor()
# child class ko call ker ga parent class ko call nahi kerni ha

# example 2

class A:
    @staticmethod
    def info():
        return f"the animale is a very cute"
class D(A):
    @staticmethod
    def info():
        return f"Dog is barking"
    
a1 = D()
print(a1.info())
# this method is same so this concept is make on notes please see it


# multi_level inheritence
class A:
    @staticmethod
    def info():
        return "A is show"
class B(A):
    @staticmethod
    def info():
        return "B is show"
class C(B):
    @staticmethod
    def info():
        return "C is show"
obj = C()
print(obj.info())

# example no 2
class Device:
    def info(self):
        print(f"this is the electronic devices") 
class Laptop(Device):
    def info(self):
        print(f"this is my laptop") 
class Gaminglaptop(Laptop):
    def info(self):
        print(f"this laptop is gaming laptop wooo i like this")

# l = Device()
# l = Laptop()
l = Gaminglaptop()
l.info() 

# example 3
class Grandfather:
    def show_grandfather(self):
        print("I am the Grandfather")

class Father(Grandfather):
    def show_father(self):
        print("I am the Father")

class Son(Father):
    def show_son(self):
        print("I am the Son")

s = Son()
s.show_grandfather()
s.show_father()
s.show_son()
# humchild class ka name le ker parent or grandparent class ke bhi method ko 
# print ker sekta ha ager method ke name different hua tub
'''other wise ya same hua tu humrhe tu tub bhi hum parent class ke 
data ko print kerwana chata ha tu tub humeha super() ka use kerna ho ga''' 

# mutliple inheritance
class Mother:
    def cook(self):
        print("mother is cooking")
class Father(Mother):
    def drive(self):
        print("Father is driving the car")

class Son(Father,Mother):
    pass
s1 = Son()
s1.cook()
s1.drive()

# example2
class E:
    def info(self):
        print("This is E")

class F:
    def info(self):
        print("This is F")

class G(F, E):   # multiple inheritance
    pass

obj = G()
obj.info()

# example 3
class Mother:
    def cook(self):
        print("mother is cooking")
class Father:
    def drive(self):
        print("Father is driving the car")

class Son(Mother,Father):
    pass
s1 = Son()
s1.drive()
s1.cook()