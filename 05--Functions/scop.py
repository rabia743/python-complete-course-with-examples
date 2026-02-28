# the type of scope local and global

# local scope
def add():
    x = 200
    print(x)
add()

def add():
    def add2():
        x = 200
        print(x)
        add2()

add()

# global scope
x = 200
def add():
     print(x)       
add()
print(x)

# using the global keyword
x = 600
def add():
     global x
     print(x)       
add()
print(x)
