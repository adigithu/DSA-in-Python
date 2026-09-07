from math import *
def count(n):
    return int(log10(n)+1)
num=int(input("Enter a number: "))
print(f"The number of digits in num is {count(num)}")