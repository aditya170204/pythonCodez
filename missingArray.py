def missingArray(arr):
    arr2=set(arr)
    arr3=list(arr2)
    arr4=sorted(arr3)
    n= len(arr4)+1
    totalSum=n*(n+1)//2
    return totalSum-sum(arr4)

print(missingArray([1,2,3,4,5,6,8,9]))