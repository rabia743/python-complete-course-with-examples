marks1 = int(input("Enter a number 1:"))
marks2 = int(input("Enter a number 2:"))
marks3 = int(input("Enter a number 3:"))

# the total precentage is
b = 100*(marks1+marks2+marks3)/300

# if(b>=40):
#     print("you should be passed",b)

# else:
#     print("you should failed")


if(b>=40 and marks1>33 and marks2>33 and marks3>33):
    print("you should be passed",b)

else:
    print("you should failed")

# this is a second method ha