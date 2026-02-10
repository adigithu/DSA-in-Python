my_list = [10, 20, 30, 40, 50]
print("Initial list:", my_list)
my_list[1] = 200
print("After changing second element:", my_list)
my_list.append(600)
print("List after appending 600:", my_list)
my_list.insert(2, 300)
print("List after inserting 300 at index 2:", my_list)
my_list.remove(600)
print("List after removing 600 (by value):", my_list)
del my_list[0]
print("List after removing element at index 0:", my_list)