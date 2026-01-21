nums=[5,9,1,2,4,15,6,3]
n=len(nums)
target=int(input("Enter the target variable: "))
hash_map=dict()
for i in range(0, n):
    remaining=target-nums[i]
    if remaining in hash_map:
        print([hash_map[remaining], i])
        break
    hash_map[nums[i]]=i