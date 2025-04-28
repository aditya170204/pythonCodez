def getMinDiff(arr,k):
        
        arr.sort()
        diff=arr[-1]-arr[0]
        for i in range(len(arr)-1):
            lower=min(arr[0]+k,arr[i+1]-k)
            upper=max(arr[-1]-k,arr[i]+k)
            diff=min(diff,upper-lower)
        return diff

print(getMinDiff([1, 5, 8, 10],2))