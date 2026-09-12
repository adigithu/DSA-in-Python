def func(n):
    if n==0 or n==1:
        return n
    num=func(n-1)+func(n-2)
    return num

num=int(input("Enter a number: "))
print(func(num))