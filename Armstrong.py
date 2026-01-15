n=int(input("Enter a number: "))
num=n
result=0
length=len(str(n))
while(num>0):
    rem=num%10
    result=rem**length+result
    num//=10
if(n==result):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")