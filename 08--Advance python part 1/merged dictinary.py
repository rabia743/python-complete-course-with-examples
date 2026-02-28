d1 = {"harry":29,"larry":56}
d2 = {"narry":80}
# is mein new dictionary ben a jate ha like merged
merged = d1|d2
print(merged)

d1 = {"harry":29,"larry":56}
d2 = {"narry":80}
# is mein d1 dictionary ko hi update kia jata ha 
d1 |= d2
print(d1)


# with statement

with open ("donkey.txt","r") as f1 , open ("donkey.txt","r") as f2:
    print(f1.read())
    print(f2.read())

    # hum at a time multiple files ko read ker sekta ha 
    # or write bhi kerwa sekta ha


with open ("donkey.txt","r") as f1 , open ("monkey.txt","w") as f2:
    print(f1.read())
    f2.write("by")
     
     
