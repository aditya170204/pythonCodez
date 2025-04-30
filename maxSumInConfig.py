

#Find the maximum value of the sum of i*arr[i] for all 0 <= i <= arr.size()-1, where arr[i] is the element at index i in the arr[]. The only operation allowed is to rotate(clockwise or counterclockwise) the array any number of times.

def maxSum( arr): 
        
        n=len(arr)
        sumi=sum(arr)
        
        currVal=sum(i*arr[i] for i in range(n))
        maxi=currVal
        
        for j in range(1,n):
            currVal=currVal+sumi-n*arr[n-j]
            maxi=max(maxi,currVal)
        return maxi

print(maxSum( [8, 3, 1, 2]))