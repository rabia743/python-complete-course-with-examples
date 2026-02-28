# making a calculator with using function
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Error you division by the zero"
    
num1 = float(input("Enter a first value:"))
num2 = float(input("Enter a second value:"))
# the operator 
print("the chosse operator +,-,*,/")
operator = input("the select theoperator is:")

if operator == '+':
    print("result:",add(num1,num2))
elif operator == '-':
    print("result:",subtract(num1,num2))
elif operator == '*':
    print("result:",multi(num1,num2))
elif operator == '/':
    print("result:",div(num1,num2))
else:
    print("invalid operator")