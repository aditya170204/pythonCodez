def findFloor(arr, x):
        
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<=x :
                return i        
        return -1

print(findFloor([1, 2, 8, 10, 10, 12, 19],5))