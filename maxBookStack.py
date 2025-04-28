k=7
m=5
arr=[4,3,6,2,1,5,7]
sumi=0
maxi=0
for i in range(len(arr)):
    if arr[i]<=m:
        sumi+=arr[i]
    elif arr[i]>m:
        sumi=0
    maxi=max(sumi,maxi)
print(maxi)


def max_Books(n, k, arr):
        
        sumi=0
        maxi=0
        for i in range(n):
            if arr[i]<=k:
                sumi+=arr[i]
            else:
                sumi=0
            maxi=max(sumi,maxi)
        return maxi
print(max_Books(7,5,[4,3,6,2,1,5,7]))