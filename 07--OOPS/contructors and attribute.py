class Student:
    name = "sara"

s1 = Student()
print(s1.name)


# default contructor
class A:
    def __init__(self):
        print("i am a default contructor")
obj = A()


# with  parameter contructor
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("rabia")
print(s1.name)

# parameter contructors
class Student:
    def __init__(self,name,age,subject,marks):
        self.name = name
        self.age = age
        self.subject = subject
        self.marks = marks

s1 = Student("rabia",20,"ai developing",70)
print(f"{s1.name},is {s1.subject},and {s1.age},{s1.marks}")

# non-parameter contructors
class Car:
    def __init__(self):
        self.name = "BMW"
        self.color = "black"
c1 = Car()
print(c1.name,c1.color)
# second example of non-parameter contructors
class Student:
    def __init__(self):
        self.name = "rabia"  
        self.age = 20
        self.subject = "ai developing"
        self.marks = 70

s1 = Student()
print(f"{s1.name},is {s1.subject},and {s1.age},{s1.marks}")

# attribute concept
class Student:
    school = "ABC School"   # class attribute

    def __init__(self, name):
        self.name = name     # instance attribute
