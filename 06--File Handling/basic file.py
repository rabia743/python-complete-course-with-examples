# file data ko read or write  from file kerna ke lia use hota ha
# the first method is read the data from file

# str = "Rabia ia a good girl"

# by default without r
f = open("file.txt")

f = open("file.txt","r")
data = f.read()
print(data)
f.close()


# the second method id data ko write kerna ke lia

f = open("my fist file","w")
f.write("hello this is my first file creating the python syantax")
f.close()

# jesa hi hum run kera ga tu aik file ben jaye gi