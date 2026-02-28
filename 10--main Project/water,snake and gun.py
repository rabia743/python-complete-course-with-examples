import random
# i will making the game snake,water,gun game
# Game values:
# snake = 1
# gun = 0
# water = -1

computer = random.choice([1, -1, 0])
youstr = (input("Enter your choice:"))
youdic = {"s":1, "w":-1,"g":0}
reversedic = {1:"snake", -1:"water",0:"gun"}
you = youdic[youstr]
print(f" you choice {reversedic[you]}\ncomputer chose {reversedic[computer]}")



if(computer == you):
    print("your choice is draw")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("somethng went wrong!")
