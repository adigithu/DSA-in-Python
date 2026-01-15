k=int(input("Enter the number of places: "))
nums=[3,9,5,6,7,2]
n=len(nums)
rotations=k%n
for _ in range(0, rotations):
    e=nums.pop()
    nums.insert(0, e)
print(nums)