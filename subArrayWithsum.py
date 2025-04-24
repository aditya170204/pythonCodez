def subArraySum(arr):
    count=0
    for i in range(len(arr)-2):
        if arr[i]+arr[i+2]==arr[i+1]:
            count+=1
    return count


print(subArraySum([1,2,1,3,5,2,4,2,6]))