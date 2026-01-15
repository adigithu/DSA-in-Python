nums= [int(x) for x in input("Enter numbers: ").split()]
freq_map=dict()
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print(freq_map)
print(freq_map[3])