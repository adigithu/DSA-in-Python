n=5
spaces=2*n-2
for i in range(1, 2*n):
    stars=i
    if(i>n):
        stars=2*n-i
    for j in range(0, stars):
        print("*", end=" ")
    for k in range(0, spaces):
        print(" ", end=" ")
    for l in range(0, stars):
        print("*", end=" ")
    print()
    if i<n:
        spaces-=2
    else:
        spaces+=2