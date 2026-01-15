nums=[3,9,5,6,7,8]
n=len(nums)
k=int(input("Enter the number of places: "))
nums[:]=nums[n-k:]+nums[:n-k]
print(nums)