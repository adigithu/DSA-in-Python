s=input("Enter a string:")
words=s.split()
words=words[::-1]
result=" ".join(words)
print(result)