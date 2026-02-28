# finally chala ga hi caha code theek ho ya us mein error ho
try:
    a = int(input("enter the list valuse:"))
    print(a)

except ValueError:
        raise TypeError("please give the correct value")
    
finally:
    print("hello i am fnally")


# example 2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result is:", result)

except ValueError:
    print("❌ ValueError: Sirf number dena chahiye, alphabets ya words nahi!")

except ZeroDivisionError:
    print("❌ ZeroDivisionError: 0 se divide nahi ho sakta!")

except TypeError:
    print("❌ TypeError: Data types match nahi ho rahe!")

except NameError:
    print("❌ NameError: Koi variable use ho raha hai jo define nahi hai!")

except IndexError:
    print("❌ IndexError: List ya index galat use ho raha hai!")

except FileNotFoundError:
    print("❌ FileNotFoundError: Jis file ka naam diya wo nahi mil rahi!")

except Exception as e:
    print(f"⚠️ Unknown Error: {e}")  # Baki sab general errors yahan ayenge.

finally:
    print("⭐ Finally: Program yahan tak pohanch gya — ye block hamesha chalta hai!")
