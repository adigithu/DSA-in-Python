def largest(arr):
    largest=float("-inf")
    for i in range(0, len(arr)):
        if nums[i]>largest:
            largest=nums[i]
    return largest
   
nums=list(map(int, input("Enter a list of numbers: ").split()))
print("The largest number in the array is", largest(nums))