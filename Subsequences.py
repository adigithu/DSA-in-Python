def func(ind, subset):
    if ind>=len(a):
        result.append(subset.copy())
        return
    subset.append(a[ind])
    func(ind+1, subset)
    subset.pop()
    func(ind+1, subset)
a=eval(input("Enter an array:"))
result=[]
func(0, [])
print(result)