def Bubble_Sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



nums=list(map(int, input("Enter a list of numbers to be sorted: ").split()))
print("The sorted list is ", Bubble_Sort(nums))