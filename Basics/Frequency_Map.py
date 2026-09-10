nums=list(map(int, input("Enter a list of numbers: ").split()))
freq={}
for i in range(0, len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1
print(freq[2])