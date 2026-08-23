nums=list(input("Enter the elements: ").split())
longest=max(nums, key=len)
print(f"The longest string in the list is {longest}")