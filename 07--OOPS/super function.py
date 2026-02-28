''' super funtion se hum parent class ka bhi method or attribute
ko print kerwa sekta ha '''
# example 1 show the method of parent class
class A:
    def __init__(self,name):
        self.name = name
    def info(self):
        print (f"hello how are yu")

class B(A):
    def info(self):
        super().info()
        print(f"My name is {self.name}")
    
d = B("sania")
d.info()

# example 2
class Mother:
    def cook(self):
        print(f"My special cooking is niahri")

class Daughter(Mother):
    def cook(self):
        super().cook()
        print(f"mom please tell us me what is your favourite cooking")

c = Daughter()
c.cook()

# attributes ko print kerwana with the help of super()
class P:
    def __init__(self,name):
        self.name = name

class C(P):
    def __init__(self, name):
        super().__init__(name)
        print(f"my name is {self.name}")

f = C("rabia")


# example 2
class Q:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class R(Q):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(f"my name is {self.name},and age is {self.age}")

f = R("rabia",20)


