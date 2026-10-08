nums=list(map(int, input("Enter a list of numbers: ").split()))
maxi=float("-inf")
total=0
for i in range(0, len(nums)):
    total=total+nums[i]
    maxi=max(maxi, total)
    if total<0:
        total=0
print("The maximum subarray sum in the list is", maxi)