f = open("poem.txt")
contant = f.read()
if"Twinkle" in contant:
    print("the twinlke words is present in file")

else:
    print("the twinlke words is not present in file")
f.close()