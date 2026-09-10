n="abashhbahewhbjsd"
m=["a", "c", "b", "d"]
hash_list=[0]*25
for num in n:
    ascii_val=ord(num)
    pos=ascii_val-97
    hash_list[pos]+=1
for num in m:
    ascii_val=ord(num)
    pos=ascii_val-97
    print(f"{num} occurs {hash_list[pos]} times")