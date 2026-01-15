nums=[1,0,2,4,3,0,5,1,0,0]
n=len(nums)
temp=[]
for i in range(0, n):
    if nums[i]!=0:
        temp.append(nums[i])
n2=len(temp)
for i in range(0, n2):
    nums[i]=temp[i]
for i in range(n2, n):
    nums[i]=0
print(nums)