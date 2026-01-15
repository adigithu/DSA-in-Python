nums=[55,32,-97,99,3,-2]
largest=nums[0]
for i in range(0, len(nums)):
    if nums[i]>largest:
        largest=nums[i]
print(f"The largest number in the given list is {largest}")