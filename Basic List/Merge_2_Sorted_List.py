def merge(arr1, arr2):
    n, m=len(arr1), len(arr2)
    i, j=0, 0
    result=[]
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            if len(result)==0 or arr1[i]!=result[-1]:
                result.append(arr1[i])
            i+=1
        else:
            if len(result)==0 or arr2[j]!=result[-1]:
                result.append(arr2[j])
            j+=1
    while i<n:
        if len(result)==0 or arr1[i]!=result[-1]:
            result.append(arr1[i])
        i+=1

    while j<m:
        if len(result)==0 or arr2[j]!=result[-1]:
            result.append(arr2[j])
        j+=1
    return result

nums1=list(map(int, input("Enter a list of numbers in sorted order: ").split()))
nums2=list(map(int, input("Enter a list of numbers in sorted order: ").split()))
print("Final Sorted list is", merge(nums1, nums2))