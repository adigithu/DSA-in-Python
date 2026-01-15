nums= [int(x) for x in input("Enter numbers: ").split()]
hash_map=dict()
for i in range(0, len(nums)):
    hash_map[nums[i]]=hash_map.get(nums[i], 0)+1
print(hash_map)
print(hash_map[3])