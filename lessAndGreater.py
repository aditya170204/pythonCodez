
def getMoreAndLess( arr, target):
    less=0
    greater=0
    for num in arr:
        if num <= target:
		        less=less+1
        elif num >= target:
		        greater=greater+1
    return [less, greater]
print(getMoreAndLess([1,2,34,5,6,7,8,],6))
		 