# raise keyword ki help se hum kisi bhi error ko generte ker sekta ha
def add():
     a = int(input("Enter a number:"))
     b = int(input("Enter b number:"))
    
     if b != 0:
          result = a/b
          print(f"the result is {result} ")
     elif b == 0:
          raise ZeroDivisionError("b=0 is not allowed")
     
add()


# example 2
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if b == 0:
    raise ZeroDivisionError("0 se divide nahi hota!")
    
print(a / b)


# example 3
def withdraw(amount):
    if amount < 0:
        raise ValueError("Negative amount withdraw nahi ho sakta!")
    print(f"{amount} withdraw ho gaya!")

withdraw(int(input("Amount: ")))


    
     
        
     
    
     


