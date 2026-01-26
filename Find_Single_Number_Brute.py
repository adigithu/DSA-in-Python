def singleNumber(arr):
    hash_map = {}
    for num in arr:
        hash_map[num] = hash_map.get(num, 0) + 1
    for key in hash_map:
        if hash_map[key] == 1:
            return key
arr = [5, 1, 3, 3, 7, 1, 7]
print(singleNumber(arr))