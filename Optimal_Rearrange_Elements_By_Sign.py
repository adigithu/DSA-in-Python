nums=[5,10,-3,-1,-10,6]
res=[0]*len(nums)
pos, neg=0, 1
for i in range(0, len(nums)):
    if nums[i]>=0:
        res[pos]=nums[i]
        pos+=2
    else:
        res[neg]=nums[i]
        neg+=2
print(res)