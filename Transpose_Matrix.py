nums=[[5,9,1],[2,3,7]]
rows=len(nums)
cols=len(nums[0])
result=[[0]*rows for _ in range(cols)]
print(result)
for i in range(rows):
    for j in range(cols):
        result[j][i]=nums[i][j]
print(result)