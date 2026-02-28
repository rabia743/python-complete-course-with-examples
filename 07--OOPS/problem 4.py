class Complex():
    def __init__(self,i,r):
        self.i = i
        self.r = r
    def __add__(self,other):
        return self.i + other.i, self.r + other.r
    def __mul__(self, other):
        return self.i * other.i, self.r * other.r
    
a = Complex(2,3)
b = Complex(4,5)
c = a + b
d = a * b
print(c)
print(d)

