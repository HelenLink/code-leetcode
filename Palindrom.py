"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""

x = int(input())

def palindrom():
    if str(x) == str(x)[::-1]:
        return True
    return False

print(palindrom())