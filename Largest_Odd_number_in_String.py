def string(n):
    b=len(num)
    for i in range(b-1, -1, -1):
        if int(n[i])%2==1:
            return n[0:i+1]
    return ""
num="68329658420"
a=string(num)
print(a)
print(type(a))