def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

nums=list(map(int, input("Enter a list of numbers: ").split()))
print("The sorted list is ", Insertion_Sort(nums))