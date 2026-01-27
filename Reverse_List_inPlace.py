val=eval(input("Enter a list:"))
s=len(val)
mid=s//2
neg=-1
for i in range(0, mid):
    val[i], val[neg]=val[neg], val[i]
    neg-=1
print("The reversed list is", val)