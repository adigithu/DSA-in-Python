def remove(str):
    result=""
    count=0
    for ch in str:
        if ch=="(":
            count+=1
            if count>1:
                result+=ch
        else:
            count-=1
            if count>0:
                result+=ch
    return result

s=input("Enter a string: ")
print("The result is", remove(s))