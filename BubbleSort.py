def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    
    return arr


print(bubbleSort([3,4,6,5,1,7,9,8,0,2]))