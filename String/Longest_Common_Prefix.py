def Prefix(str):
    if len(str)==0:
        return ""
    result=""
    base=str[0]
    for i in range(0, len(base)):
        for word in str[1:]:
            if i == len(word) or word[i]!=base[i]:
                return result
        result+=base[i]
    return result

strs=input("Enter a list of strings: ").split()
print("The longest common prefix is", Prefix(strs))