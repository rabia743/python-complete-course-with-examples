def gen():
    l = [1,2,3,4]
    for x in l:
        yield x

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# example 2
def gen():
    for i in range(1, 6):
        yield i

for x in gen():
    print(x)

# example 3
def even_gen():
    for i in range(2, 11, 2):
        yield i
# flying generater
for y in even_gen():
    print(y)
# example 4
def demo():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

for x in demo():
    print(x)
