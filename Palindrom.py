"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""

x = int(input())

def palindrom():
    return str(x) == str(x)[::-1]


print(palindrom())
