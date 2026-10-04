nums=list(map(int, input("Enter a list of numbers: ").split()))
n=len(nums)
temp=nums[n-1]
for i in range(n-2, -1, -1):
    nums[i+1]=nums[i]
nums[0]=temp
print("The list after rotation by one place is", nums)