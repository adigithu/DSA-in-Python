def String(n):
    b=n[0]
    result=""
    for i in range(0, len(b)):
        for word in n[1:]:
            if i==len(word) or word[i]!=b[i]:
                return result
        result+=b[i]
    return ""
str=["Flower", "Flow", "Flown"]
a=String(str)
print(a)