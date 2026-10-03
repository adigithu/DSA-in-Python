num=list(map(int, input("Enter numbers: ").split()))
product=1
for a in num:
    product=a*product
print(f"The product of the given list is {product}")