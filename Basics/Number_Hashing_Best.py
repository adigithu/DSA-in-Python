n=[4,3,7,7,2,4,2,1]
m=[3,6,8,0,2]
hash=dict()
for num in range(0, len(n)):
    hash[n[num]]=hash.get(n[num],0)+1
for num in m:
    if num<1 or num>10:
        print(f"{num} occurs 0 times")
    else:
        print(f"{num} occurs {hash.get(num, 0)} times")