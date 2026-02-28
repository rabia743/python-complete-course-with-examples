# the match is working like switch
n = int(input("Enter a number:"))

match n:
    case 1:
        print("the number is 1")
    case 2:
        print("the number is 2")
    case 3 | 4:
        print("the number is 3 and 4")
    case _:
        print("the invalid number")
# second example
day = input("Enter a day:")

match day:
    case "monday":
        print("the day is awsome")
    case "friday":
        print("the day near the holy days")
    case "sunday":
        print("today is holyday")
    case _:
        print("the normal day")