a=b=c=24
#multivariables ko aik hi value assigne kerwna ke lia
print(a)
print(b)
print(c)
"""multivalues ko aik hi variables mein store kerwana ke lia
using list,tuple,set and dictionary"""
#list method
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
fruits.append("orange")  
print(fruits)      # ["apple", "banana", "mango", "orange"]
#set method
numbers = {1, 2, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4}
numbers.add(5)
print(numbers)   # {1, 2, 3, 4, 5}
#tuple method
coordinates = (10, 20)
print(coordinates[0])   # 10
# coordinates[0] = 50   ❌ Error (cannot modify)

