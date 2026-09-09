n=int(input("Enter a number: "))
l=len(str(n))
num=n
total=0
while num>0:
    rem=num%10
    total=rem**l+total
    num=num//10
if(total==n):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")