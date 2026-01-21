n=5
for i in range(0, n):
    ch=69
    for j in range(0, i+1):
        print(chr(65+n-i-1+j), end=" ")
    print()