import heapq as heap
def kthSmallest(arr,k):
    d={}
    kth = None
    heap.heapify(arr)
    for i in range(k):
        kth=heap.heappop(arr)
    return kth
print(kthSmallest([0,9,4,3,7,6,5,1,2,8],5))
