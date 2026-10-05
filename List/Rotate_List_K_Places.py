def reverse(arr, left, right):
    while left<right:
        arr[left], arr[right]=arr[right],arr[left]
        left+=1
        right-=1

nums=list(map(int, input("Enter a list of numbers: ").split()))
k=int(input("Enter the number of rotations: "))
n=len(nums)
reverse(nums, n-k, n-1)
reverse(nums, 0, n-k-1)
reverse(nums, 0, n-1)
print("The final list after rotations is", nums)