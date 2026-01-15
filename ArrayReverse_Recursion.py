def reverse_func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_func(arr, left + 1, right - 1)
def reverseArray(nums):
    reverse_func(nums, 0, len(nums) - 1)
    return nums
nums = [2, 4, 1, 7, 6, 3, 8, 9, 5]
print("Original array:", nums)
print("Reversed array:", reverseArray(nums))