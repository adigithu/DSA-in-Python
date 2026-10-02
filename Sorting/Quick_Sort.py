def partition(nums, low, high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>=pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i], nums[j]=nums[j], nums[i]
    nums[low], nums[j]=nums[j], nums[low]
    return j

def Quick_Sort(arr, low, high):
    if low<high:
        ind=partition(arr, low, high)
        Quick_Sort(arr, low, ind-1)
        Quick_Sort(arr, ind+1, high)
    return arr
nums=list(map(int, input("Enter a list of numbers: ").split()))
print("The sorted list is ", Quick_Sort(nums, low=0, high=len(nums)-1))