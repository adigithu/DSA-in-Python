nums=list(map(int, input("Enter numbers: ").split()))
largest=float("-inf")
for i in range(0, len(nums)):
    largest=max(largest, nums[i])
print("The largest number in the list is", largest)