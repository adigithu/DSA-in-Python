n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_dict={}
for i in range(len(n)):
    if n[i] in hash_dict:
        hash_dict[n[i]]+=1
    else:
        hash_dict[n[i]]=1
for nums in m:
    if nums<0 or nums>11:
        print(0)
    else:
        print(hash_dict.get(nums, 0))