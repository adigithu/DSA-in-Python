def roman(str):
    letters={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result=0
    n=len(str)
    for i in range(0, n):
        if i<n-1 and letters[str[i]]<letters[str[i+1]]:
            result-=letters[str[i]]
        else:
            result+=letters[str[i]]
    return result

s=input("Enter a string: ")
print(roman(s))