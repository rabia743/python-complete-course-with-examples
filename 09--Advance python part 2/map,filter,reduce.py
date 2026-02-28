from functools import reduce
'''map(): Applies a function to each element of an iterable.

filter(): Filters elements based on a condition.

reduce(): Reduces iterable to a single value.
(function, iterable)'''

l = [1,2,3,4,5]
l = (list(map(lambda x: x * 2,l)))
print(l)

l = [1,2,3,4,5]
l = (list(filter(lambda x: x % 2 == 0,l)))
print(l)

m = [1,2,3,4,5,6]
m = reduce(lambda a,b: a + b,m)
print(m)