s=input("Enter a string:")
sum=0
for i in s:
    if i.lower() in 'aeiou':
        sum=sum+1
print(sum)