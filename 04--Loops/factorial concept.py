# using the more clear concept of factorial
# Take a number as input and print the factorial of all numbers from 1 to that number.
# (Example: if input is 5 → output factorials of 1, 2, 3, 4, 5)

n = int(input("Enter a number:"))
product = 1
for x in range(1,n+1):
    product = product*x

print(f" the number is {n} and the factorial is {product}")

# using the for loop