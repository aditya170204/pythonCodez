def findDuplicates(arr):
    seen = set()
    duplicates= set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(findDuplicates([2 ,3 ,1 ,2, 3,3,4,6,7,8,0,9,8,75,3,31,32,45,6,8]))