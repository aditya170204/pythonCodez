def bobbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bobbleSort([2,3,4,76,6,7,90,98,76,54,321,2,34,567,89,0,98,7,65]))