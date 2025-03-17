def kLargest(arr,k):
    if len(arr)<k:
        return -1
    sortAr=sorted(arr,reverse=True)
    return sortAr[:k]

print(kLargest([9,8,7,6,5,33,4,5,6,78,9,0,85,4,3,34,56,78,90,98,76,5,43,45,6,78,90,9,87,65,43,2,123,4,56,8,5,63],3))

