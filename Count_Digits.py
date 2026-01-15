n=int(input("Enter a number: "))
num=n
count=0
while(num>0):
    count=count+1
    num//=10
print(f"The count of digits in {n} is {count}")