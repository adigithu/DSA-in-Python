nums = [2, 4, 1, 7, 6, 3, 8, 9, 5]
print("Original array:", nums)
left, right=0, len(nums)-1
while left<=right:
    nums[left], nums[right]=nums[right], nums[left]
    left, right=left+1, right-1
print("Reversed array:", nums)