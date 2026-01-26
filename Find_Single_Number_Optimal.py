def singleNumber(arr):
    ans = 0
    for num in arr:
        ans = ans ^ num
    return ans
arr = [5, 1, 3, 3, 7, 1, 7]
print(singleNumber(arr))