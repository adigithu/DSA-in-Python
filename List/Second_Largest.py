def Second_Largest(arr):
    largest=float("-inf")
    s_largest=float("-inf")
    for i in range(0, len(arr)):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
    return s_largest

nums=list(map(int, input("Enter a list of numbers: ").split()))
print("The second largest element in the list is", Second_Largest(nums))