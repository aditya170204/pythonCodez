
'''The equilibrium point in an array is an index such that the sum of all elements before that index
 is the same as the sum of elements after it.'''

def findEquilibrium(arr):
        # code here
        tsum=sum(arr)
        lsum=0
        for i,num in enumerate(arr):
            if lsum == (tsum-lsum-num):
                return i
            lsum+=num
        return -1

print(findEquilibrium([-7, 1, 5, 2, -4, 3, 0]))