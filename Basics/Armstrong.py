n=int(input("Enter a number:"))
num=n
a=len(str(n))
total=0
while num>0:
    ld=num%10
    total=total+ld**a
    num=num//10
if total==n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")