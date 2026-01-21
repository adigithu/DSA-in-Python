n=5
for i in range(0,n):
    for j in range(0, n-i-1):
        print(" ", end=" ")
    bp=(2*i+1)//2
    ch=65
    for k in range(0, 2*i+1):
        print(chr(ch), end=" ")
        if (k<bp):
            ch=ch+1
        else:
            ch=ch-1
    for j in range(0, n-i-1):
        print(" ", end=" ")
    print()