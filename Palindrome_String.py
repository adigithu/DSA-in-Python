s=input("Enter a string: ")
left, right=0, len(s)-1
a=True
while left<=right:
    if s[left] != s[right]:
        a=False
    left+=1
    right-=1
if(a==True):
    print(f"{s} is a palindrome string")
else:
    print(f"{s} is not a palindrome string")