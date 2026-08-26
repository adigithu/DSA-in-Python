str=input("Enter a string: ")
for char in str:
    if str.lower().count(char) == 1:
        print(f"The non-repeated character in {str} is {char}")
        break