# example 1
def user(fnx):
    def mfx():
        print("hello guys")
        fnx()
        print("take care!")
    return mfx

@user
def say():
    print("hello world")

say()
# def user(fnx): per likha ha same @decurater mein likna ha


# example 2
def user(fnx):
    def mfx(*args,**kwargs):
        print("hello guys")
        fnx(*args,**kwargs)
        print("take care!")
    return mfx

@user
def add(a,b):
    print(a + b) 
a = add(2,3)

# example 3 with return 
def user(fnx):
    def mfx(*args,**kwargs):
        print("hello guys")
        result = fnx(*args,**kwargs)
        print("take care!")
        return result
    return mfx

@user
def mul(a,b):
    return(a * b) 
a = mul(2,3)
print(a)