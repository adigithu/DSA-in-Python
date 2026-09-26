def Selection_Sort(arr):
    for i in range(0, len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index], arr[i]
    return arr
nums=list(map(int, input("Enter a list of numbers: ").split()))
print("Sorted array is ", Selection_Sort(nums))