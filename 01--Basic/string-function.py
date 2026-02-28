# slicing string
x = "rabia"
print(x[0:4])
# is mein starting tu print ho ga but last wala print nahi ha ga 
# acording to rules
y = "rabia zafar"
print(y[2:7])

z = "hello,world"
print(z[-7:-3])
print(z[4:8])

# Modify string
# 1  upper string
a = "Hello, World!"
print(a.upper())
# 2 lower string
a = "Hello, World!"
print(a.lower())
# 3 Remove whitespace string
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# 4 replace string
a = "Hello, World!"
print(a.replace("H", "J"))
# 5 spilt string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
