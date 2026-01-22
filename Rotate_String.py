a=input("Enter a string:")
goal=input("Enter a string:")
if len(a)!=len(goal):
    print(f"{goal} is not a part of {a}")
else:
    double_S=a+a
    if goal in double_S:
        print(f"{goal} is a part of {a}")
    else:
        print(f"{goal} is not a part of {a})")