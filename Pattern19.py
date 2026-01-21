n=5
inis=0
for i in range(0,n):
    for j in range(n-i, 0, -1):
        print("*", end=" ")
    for k in range(0, inis):
        print(" ", end=" ")
    for l in range(n-i, 0, -1):
        print("*", end=" ")
    inis+=2
    print()
inis=8
for i in range(0,n):
    for j in range(0, i+1):
        print("*", end=" ")
    for k in range(0, inis):
        print(" ", end=" ")
    for l in range(0, i+1):
        print("*", end=" ")
    inis-=2
    print()