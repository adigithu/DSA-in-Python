def selection_Sort(arr):
    for i in range(0, len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index], arr[i]
    return arr

nums=list(map(int, input("Enter a list of numbers: ").split()))
print(selection_Sort(nums))