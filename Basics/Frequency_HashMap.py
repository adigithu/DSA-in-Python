n = int(input("Enter number of elements: "))
nums = []
print("Enter the elements:")
for i in range(n):
    nums.append(int(input()))
hash_map = {}
for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1
print("\nFrequency of each element:")
for key, value in hash_map.items():
    print(f"{key} : {value}")