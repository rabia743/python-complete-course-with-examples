# there are two types of read file 
# no 1 is readline
# no 2 is readlines


f = open("file.txt")
data = f.readline()
print(data)
f.close()


file = open("file.txt", "r")

line1 = file.readline()   # First line
line2 = file.readline()   # Second line
line3 = file.readline()   # Second line

print(line1)
print(line2)
print(line3)

file.close()


# method 2
f = open("file.txt")
lines = f.readlines()
print(lines)
f.close()
# ya sub lines ko list mein lik ker dta ha[] 