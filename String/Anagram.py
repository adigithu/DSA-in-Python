def anagram(s,t):
    if len(s) != len(t):
        return False
    char_freq={}
    for ch in s:
        char_freq[ch]=char_freq.get(ch, 0)+1
    for ch in t:
        if ch not in char_freq:
            return False
        else:
            if char_freq[ch] == 0:
                return False
            else:
                char_freq[ch] -=1
    return True

s=input("Enter first string: ")
t=input("Enter the second string: ")
print(anagram(s,t))