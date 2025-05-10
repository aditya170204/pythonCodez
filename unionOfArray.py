'''Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.'''



def findUnion(a,b):
        
        return sorted(list(set(a+b)))

print(findUnion([1, 2, 3, 4, 5],[1, 2, 3, 6, 7]))