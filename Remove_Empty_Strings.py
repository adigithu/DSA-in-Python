list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list1)
for i in list1:
    if i=="":
        list1.remove(i)
print(list1)