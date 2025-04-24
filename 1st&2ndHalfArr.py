def compareHalfs(arr):
    
    n=len(arr)
    f=0
    s=0
    for i in range(n):
        if i<n//2:
            f+=arr[i]
        else:
            s+=arr[i]
    if s>f:
        return arr[::-1]
    else:
        return "condition doesn't match" 

print(compareHalfs([19,1,2,3,4,5,6]))