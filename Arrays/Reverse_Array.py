class Solution:
    def reverseArray(self, arr):
        def reverse(left, right):
            if left>right:
                return
            arr[left], arr[right]=arr[right], arr[left]
            reverse(left+1,right-1)
        reverse(0, len(arr)-1)
        return arr
nums=list(map(int, input("Enter list of numbers: ").split()))
a=Solution()
print("The reversed array is ", a.reverseArray(nums))