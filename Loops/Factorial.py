num=int(input("Enter a number: "))
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(f"The factorial of the given number is {fact}")