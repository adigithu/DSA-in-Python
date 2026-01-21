nums=[7,2,1,5,6,4,8]
n=len(nums)
min_price=float("inf")
max_profit=0
for i in range(n):
        min_price=min(min_price, nums[i])
        max_profit=max(max_profit, nums[i]-min_price)
print(max_profit)