nums=list(map(int, input("Enter a list of numbers: ").split()))
pos=[]
neg=[]
for num in nums:
    if num>0:
        pos.append(num)
    else:
        neg.append(num)

i=0
j=0
k=0

while i<len(pos) and j<len(neg):
    nums[k]=pos[i]
    i+=1
    k+=1

    nums[k]=neg[j]
    j+=1
    k+=1

while i<len(pos):
    nums[k]=pos[i]
    i+=1
    k+=1

while j<len(pos):
    nums[k]=neg[j]
    j+=1
    k+=1

print(nums)