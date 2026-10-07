def Two_Sum(arr, target):
    hash_map={}
    for i in range(0, len(nums)):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]]=i
    return []

nums=list(map(int, input("Enter a list of numbers: ").split()))
target=int(input("Enter a target: "))
print(Two_Sum(nums, target))