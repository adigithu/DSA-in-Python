a=[1, 7, 8, 4, 5, 6, 9, 2]
n=len(a)
for i in range(0, n):
    min_index=i
    for j in range(i+1, n):
        if a[j] < a[min_index]:
            min_index=j
    a[i], a[min_index]=a[min_index], a[i]
print(f"Sorted list: {a}")