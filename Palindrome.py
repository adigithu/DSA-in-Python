n=int(input("Enter a number: "))
num=n
result=0
while(num>0):
    rem=num%10
    result=result*10+rem
    num//=10
if(n==result):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")