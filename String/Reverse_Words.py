def Reverse(str):
    words=str.split()
    words.reverse()
    result=" ".join(words)
    return result    

s=input("Enter input string: ")
print(Reverse(s))