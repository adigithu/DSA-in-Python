nums=list(map(int, input("Enter a list of numbers: ").split()))
n=len(nums)
print("The missing number is", (n*(n+1))//2 - sum(nums))