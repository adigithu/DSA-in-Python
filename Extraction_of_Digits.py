n=int(input("Enter a number: "))
if(n==0):
    print("The digit is 0")
while(n>0):
    digit=n%10
    print(digit, end=' ')
    n//=10