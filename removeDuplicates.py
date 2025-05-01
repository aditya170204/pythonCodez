#Given a sorted array arr. Return the size of the modified array which contains only distinct elements.


def removeDuplicates(arr):
        #Code Here
        if not arr:
            return 0
        j = 0  
        for i in range(1, len(arr)):
            if arr[i] != arr[j]:
                j += 1
                arr[j] = arr[i]
    
        return j + 1

print(removeDuplicates([2, 2, 2, 2, 2,3,3,4,4,5]))