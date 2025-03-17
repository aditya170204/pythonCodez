# You are given an integer n and an integer array arr of size n+2. All elements of the array are in the range from 1 to n. Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
# Note: Return the numbers in their order of appearing twice. So, if x and y are repeating numbers, and x's second appearance comes before the second appearance of y, then the order should be (x, y).


def twoRepeated(n,arr):
    seen=set()
    dupli=[]
    for i in arr:
        if i in seen:
            dupli.append(i)
        else:
            seen.add(i)
    return dupli

print(twoRepeated(9,[1,2,3,4,5,6,7,8,4,6,9]))