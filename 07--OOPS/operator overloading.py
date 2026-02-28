# her operator ka behaviour different ho ga
# its best example of polyporism pillar
# same method different objects mean different output

class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return self.x + other.x , self.y + other.y
    def __sub__(self,other):
        return self.x - other.x , self.y - other.y
    def __ge__(self,other):
        return self.x >= other.x , self.y >= other.y
    def __le__(self,other):
        return self.x <= other.x , self.y <= other.y
    
n = A(2,3)
n1 = A(3,5)
nth = n + n1
mth = n - n1
ztg = n >= n1
let = n <= n1
print(nth)
print(mth)
print(ztg)
print(let)


# most important opertor overloading
'''
Operator / Function	Magic Method	Use / Example
+	__add__	Addition, Concatenation
-	__sub__	Subtraction
*	__mul__	Multiplication / Repeat
/	__truediv__	Division
==	__eq__	Check equality
!=	__ne__	Check inequality
<	__lt__	Less than
>	__gt__	Greater than
<=	__le__	Less than or equal
>=	__ge__	Greater than or equal
str()	__str__	Human-readable string
len()	__len__	Length of object
()	__call__	Make object callable'''

class C:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f"Value = {self.x}"

a = C(10)
print(a)  # Output: Value = 10

class D:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)

a = D([1,2,3,4])
print(len(a))  # Output: 4

class E:
    def __call__(self):
        print("Object called like a function!")

a = E()
a()  # Output: Object called like a function!
