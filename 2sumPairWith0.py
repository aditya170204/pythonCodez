def twoSumPairWith0Sum(arr):
    left=0
    right=len(arr)-1
    arr.sort()
    pair=[]

    while left<right:
        sumi=arr[left]+arr[right]
        if sumi==0:
            pair.append([arr[left],arr[right]])

            while left<right and arr[left]==arr[left+1]:
                left+=1

            while left<right and arr[right]==arr[right-1]:
                right-=1

            left+=1
            right-=1

        elif sumi>0:
            right-=1    
        else:
            left +=1

    return pair

print(twoSumPairWith0Sum([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))

            
