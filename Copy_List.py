original_list = [10, 20, 30]
print("Original list initially:", original_list)
# This is a common and concise way to create a shallow copy
copied_list = original_list[:]

# Modify the copied list
copied_list.append(40)
copied_list[0] = 100

print("Original list after modifying copy:", original_list)
print("Copied list after modification:", copied_list)

# Demonstration using list() constructor
another_copy = list(original_list)
another_copy.append(50)
print("\nOriginal list after another_copy modification:", original_list)
print("Another copied list:", another_copy)

# Demonstration using .copy() method (Python 3+)
third_copy = original_list.copy()
third_copy[0] = 999
print("\nOriginal list after third_copy modification:", original_list)
print("Third copied list:", third_copy)