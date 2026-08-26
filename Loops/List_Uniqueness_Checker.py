items=list(input("Enter a list: ").split())
unique_item=set()
for i in items:
    if i in unique_item:
        print("Duplicate:",i)
        break
    unique_item.add(i)
print(unique_item)