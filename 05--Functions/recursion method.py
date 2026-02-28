# recursion calling by itself and problem ko easy and smatest formula mein solve kerta ha
# example
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))
# how its work
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1


def sum_number(n):
    if n == 0:
        return 0
    else:
        return n + sum_number(n-1)
print(sum_number(5))




def number(n):
    if n <= 0:
        return ("done!")
    else:
        print(n)
        return number(n-1)
number(5)
    