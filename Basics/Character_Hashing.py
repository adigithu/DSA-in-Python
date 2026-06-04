S="azyxyyzaaaa"
q=["d", "a", "y", "x"]
l=[0]*26
for ch in S:
    ascii_val=ord(ch)
    index=ascii_val-97
    l[index]+=1
for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(l[index])