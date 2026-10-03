def Sorted(arr):
    for i in range(0, len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums=list(map(int, input("Enter a list of numbers: ").split()))
if (Sorted(nums)==True):
    print("The list is sorted")
else:
    print("The list is not sorted")