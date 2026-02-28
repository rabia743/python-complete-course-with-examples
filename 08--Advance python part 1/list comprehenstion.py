list = []
for list in range(1,6):
    print(list)

    # isko easy fast se bhi ker sekta ha jisa list comprehenstion kehta ha

list = [i for i in range(1,6)]
print(list)
# example 2
n = [i*i for i in range(1,6)]
print(n)

# example3
m = [i for i in range(1,6) if i%2 == 0]
print(m)
# example 4
names = ["ali", "sara", "zara"]
upper_names = [name.upper() for name in names]
print(upper_names)


# enramrate means show the index with value in lists example
a = [1,2,3,4,5,6]
for index, value in enumerate(a):
    print(index,value)

fruits = ["apple","banana","gava"]
for index, fruits in enumerate(fruits,start=1):
    print(index,fruits)

# set comprehension
set = {1,1,2,2,3,4,4,4,5,8,8,9,0}
set = {i for i in set}
print(set)