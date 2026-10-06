def Linear_Search(arr, target):
    n=len(arr)
    for i in range(0, n):
        if arr[i]==target:
            return i
    return -1
nums=list(map(int, input("Enter a list of numbers: ").split()))
target=int(input("Enter a target: "))
print(Linear_Search(nums, target))