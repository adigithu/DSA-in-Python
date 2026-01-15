nums = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
hash_dict=dict()
for i in range(0, len(nums)):
    hash_dict[nums[i]]=hash_dict.get(nums[i], 0)+1
for x in m:
    if x not in nums:
        print(f"{x} appears 0 times")
    else:
        print(f"{x} appears {hash_dict.get(nums[i], 0)} times")