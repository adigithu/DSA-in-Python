def parenthesis(str):
    max_depth=0
    curr_depth=0
    for ch in str:
        if ch=='(':
            curr_depth+=1
            max_depth=max(max_depth,curr_depth)
        elif ch==')':
            curr_depth-=1
    return max_depth

s=input("Enter a string: ")
print(parenthesis(s))