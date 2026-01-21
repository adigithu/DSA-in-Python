nums=[5,-2,3,9,0,6,10,7]
n=len(nums)
nums[:]=[nums[n-1]] + nums[0: n-1]
print(nums)