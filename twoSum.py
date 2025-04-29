def twoSum( arr, target):
        # code here
        left=0
        right=len(arr)-1
        
        while left<right:
            if arr[left]+arr[right]==target:
                return left+1,right+1
            elif arr[left]<arr[right]:
                left+=1
            elif arr[right]<arr[left]:
                right-=1
            else:
                return -1

print(twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15))