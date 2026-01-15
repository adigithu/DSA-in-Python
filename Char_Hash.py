s="azyxyyzaaaa"
q=["d", "a", "y", "x"]
hash_list=[0] * 26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1
for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(f"{ch} occurs {hash_list[index]} times")