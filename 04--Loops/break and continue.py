# break its stop the loop example 
i = 6
while i > 0:
    print(i)
    if(i==3):
        break
    i = i-1

# example 2
fruits = ["banana","apple","gava"]
for x in fruits:
    print(x)
    if(x=="apple"):
        break

# continue statement its stop the current iteration like
i = 6
while i > 0:
    i = i-1 
    if(i==3):
        continue
    print(i)

# example 2
fruits = ["banana","apple","gava"]
for x in fruits:
    if(x=="apple"):
        continue
    print(x)

    # pass statement 
for x in range (0,10,2):
    pass
# pass mean ke abhi kush mat karo just abhi skip ker do bad mein kera ga ok
