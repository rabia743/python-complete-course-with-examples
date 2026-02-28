# i have a calculator according the concept off oop

class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b != 0:
            return a/b
        else:
            print("you put the invalid value")

c = Calculator()
print(c.add(3,8))
print(c.mul(7,10))
print(c.div(9,3))
print(c.sub(99,11))
