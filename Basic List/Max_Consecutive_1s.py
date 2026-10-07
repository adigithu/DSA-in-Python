nums=list(map(int, input("Enter a list of numbers: ").split()))
count=0
max_count=0
for i in range(0, len(nums)):
    if nums[i]==1:
        count+=1
    else:
        max_count=max(count, max_count)
        count=0
print("The maximum number of consecutive 1's in the list is", max_count)