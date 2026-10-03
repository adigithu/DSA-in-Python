def Remove_Duplicates(arr):
    n=len(arr)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if nums[i]!=nums[j]:
            i+=1
            nums[i], nums[j]=nums[j], nums[i]
        j+=1
    return i+1

nums=list(map(int, input("Enter a list of elements: ").split()))
print("The number of unique elements in the given list is", Remove_Duplicates(nums))