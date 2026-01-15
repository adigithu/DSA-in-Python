from math import *
def countDigits(n):
    if(n==0):
        return 1
    return int(log10(n)+1)
n=int(input("Enter a number: "))
print(f"The count of digits in {n} is ", countDigits(n))