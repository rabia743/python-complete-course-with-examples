import random

n = random.randint(0, 100)

a = -1
guess = 0

while a != n:
    a = int(input("Enter your number: "))
    guess += 1

    if a > n:
        print("Please guess a LOWER number")
    elif a < n:
        print("Please guess a HIGHER number")

print(f"You guessed the number {a} in {guess} attempts")

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# myenv\Scripts\activate