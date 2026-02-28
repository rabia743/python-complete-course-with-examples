# using recursion method i have sum the values


def sum_number(n):
    if n == 0:
        return 0
    else:
        return n + sum_number(n-1)
print(sum_number(4))
