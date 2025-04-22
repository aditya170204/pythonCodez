def isSubset( a, b):
        # Your code here
        for i in b :
            if i in a:
                a.remove(i)
            else:
                return False
        return True
print(isSubset([2,3,4,1,6,7,8,7],[3,7,7,4]))