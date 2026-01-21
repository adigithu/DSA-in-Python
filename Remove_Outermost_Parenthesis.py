a=input("Enter a string:")
result=""
count=0
for ch in a:
    if ch=="(":
        count+=1
        if count>1:
            result+=ch
    else:
        count-=1
        if count>0:
            result+=ch
print(result)