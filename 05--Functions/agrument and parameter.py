# agrument method
def my_function(name):
    print("hello world",name)
my_function("rabia")
# its real value user give the function is called agrument example my_function("rabia")
def my_function(name):
    print(f"my name is {name}")
my_function("rabia")
# the placeholder  usd inside a function like def my_function(name) is called parameters

def add(a,b):
    print(a+b)
add(2,3)

#  default parameters
def my_fun(country="Japan"):
    print("I am from " + country)
my_fun("London")
my_fun("Switzerland")
my_fun()
my_fun("Korea")

# return concept 
# return the value from the indside function example
def my_function(name):
    print(f"my name is {name}")
    return name
a = my_function("rabia")
print(a)
# hum na jo place holder use kia ha hue hum return mein like ga like return name

def my_fun(age,name):
    print(f"my name is {name} , {age}") 
    return (name,age)
a = my_fun( 20,"rabia")
print(a)
