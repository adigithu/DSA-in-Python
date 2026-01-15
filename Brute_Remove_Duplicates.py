nums=[1,1,1,2,3,4,4,7,9,9,10]
n=len(nums)
freq_map=dict()
for i in range(n):
    freq_map[nums[i]]=0
j=0
for k in freq_map:
    nums[j]=k
    j+=1
print(nums)
print(j)