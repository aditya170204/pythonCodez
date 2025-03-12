# def third_largest(arr):
#     if len(arr)<3:
#         return -1
#     lar=1
#     seclar=2
#     thirdlar=1
#     for num in arr:
#         if num>lar:
#             thirdlar=seclar
#             seclar=lar
#             lar= num
#         elif num>seclar and num<lar:
#             thirdlar=seclar
#             seclar=num
#         elif num>thirdlar and num< seclar:
#             thirdlar=num
#     if thirdlar!=1:
#         return thirdlar
#     else:
#         return -1
# print(third_largest([23,45,6,78,987,656,4,3,2,34,56,7,89,876]))


def thirdLar(arr):
    setArr = set(arr)
    sortedArr= sorted(setArr)
    arr2 = list(sortedArr)
    n=len(arr2)
    return (arr2[-3])

print(thirdLar([9,8,7,6,5,33,4,5,6,78,9,0,85,4,3,34,56,78,90,98,76,5,43,45,6,78,90,9,87,65,43,2,123,4,56,8,5,63,]))