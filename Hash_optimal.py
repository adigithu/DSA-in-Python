n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
L = 11
hash_list = [0] * L
print(hash_list)
for num in n:
    hash_list[num] += 1
for num in m:
    if num < 1 or num > 10:
        print(f"{num} occurs 0 times")
    else:
        print(f"{num} occurs {hash_list[num]} times" )