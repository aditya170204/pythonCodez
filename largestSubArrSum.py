def largestSubArrSum(arr):
    maxi=float("-inf")
    sumi=0
    for num in arr:
        sumi=max(num,sumi+num)
        maxi=max(maxi,sumi)
        if sumi<0:
            sumi=0
    return maxi

print(largestSubArrSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
