nums=list(map(int, input("Enter a list of numbers: ").split()))
n=len(nums)
if n==1:
    print(nums)
i=0
while i<len(nums):
    if nums[i]==0:
        break
    i+=1
if i==n:
    print(nums)
j=i+1
while j<len(nums):
    if nums[j]!=0:
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
    j+=1
print(nums)