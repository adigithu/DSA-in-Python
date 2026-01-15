def func(nums):
    n=len(nums)
    for i in range(n):
        if nums[i]==target:
            return i
    return -1

nums=[5,3,9,8,1,6,4,-10,-100]
target=int(input("Enter the value of the target: "))
print(f"{target} is found at index", func(nums))