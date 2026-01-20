n=4
space=2*(n-1)
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(0, space):
        print("-", end=" ")
    for l in range(i, 0, -1):
        print(i, end=" ")
        i=i-1
    space-=2
    print()