# error ko handle kerna ke lia use hota ha 
try:
    a = int(input("Enter a number:"))
except ValueError:
    print("please enter the valid syantax")

# ager error aya tu wo is execpt mein jaye ga program crash nahi ho ga


try:
    a = int(input("Enter a number:"))
    b = int(input("Enter b number:"))
    result = a/b
    print(f"the result is {result}")

except ZeroDivisionError:
    print("zero division error please interger number under the divide")

except ValueError:
    print("please enter valid number")
# jub humera program theek ho ga wothout error ke tu wo else mein jaye ga
else:
    print("heelo i am correct and i am inside else")
    




