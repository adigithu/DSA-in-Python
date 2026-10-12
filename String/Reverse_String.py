def reversed(str):
    left=0
    right=len(str)-1
    str=list(str)
    while left<right:
        str[left], str[right]=str[right], str[left]
        left+=1
        right-=1

    return "".join(str)

s=input("Enter a string: ")
print(reversed(s))