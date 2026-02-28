a = 12
b = 34
c = 5

def number(a,b,c):
    if(a>b and a>c):
        print("the a is greatest number")
    elif(b>a and b>c):
        print("the b is greatest number")
    elif(c>a and c>b):
        print("the c is greatest number")

number(a,b,c)

# second method
def number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

number(a,b,c)