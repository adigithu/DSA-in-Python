def match(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        else:
            left+=1
            right-=1
    return True
s=input("Enter a string: ")
if (match(s)==True):
    print(f"{s} is a palindrome string")
else:
    print(f"{s} is not a palindrome string")