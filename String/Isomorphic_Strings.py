def Isomorphic(s,t):
    if len(s) != len(t):
        return False
    map_s={}
    map_t={}
    for i in range(0, len(s)):
        if s[i] in map_s:
            if map_s[s[i]]!=t[i]:
                return False
        else:
            map_s[s[i]]=t[i]
        if t[i] in map_t:
            if map_t[t[i]]!=s[i]:
                return False
        else:
            map_t[t[i]]=s[i]
    return True

s=input("Enter a string: ")
t=input("Enter the second string: ")
print(Isomorphic(s, t))