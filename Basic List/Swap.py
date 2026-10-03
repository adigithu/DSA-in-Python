nums=list(map(int, input("Enter numbers: ").split()))
nums[0], nums[1]=nums[1],nums[0]
print("The list after swapping is ", nums)