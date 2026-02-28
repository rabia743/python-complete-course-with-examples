p1 = "Makes a lot of money"
p2 = "by now"
p3 = "sucribe this"
p4 = "click this"

message = input("Enter a comment:")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This is a spam so dont this")

else:
    print("This message is not spam")

# in mean ha ke ya text kia us message ke andar ha kia