n=int(input("Enter a number:"))
num=n
pal=0
while num>0:
    rem=num%10
    pal=pal*10+rem
    num=num//10
if(n==pal):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")