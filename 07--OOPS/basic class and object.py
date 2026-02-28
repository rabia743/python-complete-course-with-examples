# oop is a object oriented programming its using to remove the redendence mean dublication and 
# reuseablitiy of your code
# basic class and object concept example
class Student:
    name = "sara"

s1 = Student()
print(s1.name)


# 2nd example
class Student:
    name = "sara"

s1 = Student()
print(s1.name)
s2 = Student()
print(s2.name)


# 3rd example
class Student:
    name = "sara"
    fees = 19000

s1 = Student()
print(s1.name)
print(s1.fees)
s2 = Student()
print(s2.name)
print(s1.fees)


