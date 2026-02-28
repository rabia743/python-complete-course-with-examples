'''It is called the assignment expression operator.
It allows you to assign a value to a variable and use it in the same expression.

Why it’s called “walrus”

Because := looks like a walrus face 🙂'''

if (n := (len({1,2,3,4,5}) > 3)):
    print(f"no your set sizi is large {n}")


# example 2
if (M := len({"harry":20,"larry":40}) > 3):
    print(f"the dictionary size is greater then\n {M}")

# ager koi condition false ho gayi ha tu error nahi aye ga bulka wo run nahi
# ho ga # example 2 its exaple

if (M := ([1,2,3,4]) < ([3,4,5])):
    print(f"the list size is smaller then\n {M}")

'''
    Data Type	< / > allowed?
int	✅ Yes
float	✅ Yes
str	✅ Yes (lexicographical)
list	✅ Yes (element-wise)
tuple	✅ Yes
dict	❌ No
set	❌ No'''