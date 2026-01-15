def count(nums):
    count=0
    max_count=0
    n=len(nums)
    for i in range(n):
        if nums[i]==1:
            count+=1
        else:
            max_count=count
            count=0
    return max(max_count, count)
nums=[1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1]
print("The count of consecutive ones is", count(nums))