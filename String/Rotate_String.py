def Rotate(s,goal):
    if len(s)!=len(goal):
        return False
    double_S=s+s
    if goal in double_S:
        return True
    return False

s=input("Enter the input string: ")
goal=input("Enter the goal string: ")
print(Rotate(s,goal))