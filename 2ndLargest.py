def second_largest_ele(arr):
    if len(arr)<2:
        return -1,"not enougn elements to get second largest"
    largest =1
    second_largest=1
    for num in arr:
        if num>largest:
            second_largest=largest
            largest=num
        elif num> second_largest and num<largest:
            second_largest=num
    return second_largest if second_largest!=1 else -1
print(second_largest_ele([1,3,5,3,9,7,5,9,6,1,34,43,54,11,3,6,78,76]))

def secLargest(arr):
    if len(arr)<2:
        return -1
    lar=1
    secLar=1
    for num in arr:
        if num>lar:
            secLar=lar
            lar=num
        elif num>secLar and num<lar:
            secLar=num
    return secLar if secLar!=1 else -1
print(secLargest([2,45,67,65,334,3,2,367,87654,67,6,43,456,7,89]))

def seclarge(arr):
    if len(arr)<2:
        return -1
    large=1
    secLarge=1
    for num in arr:
        if num>large:
            seclarge=large
            large=num
        elif num>seclarge and num<large:
             secLarge=num
    return secLarge if secLarge!=1 else -1
print(seclarge([23,45,67,89,87,65,43,23,45,67,7,88 ,56,90]))



# only largest element
def largest(arr):
    largestnum=0
    for num in arr:
        if num>largestnum:
            largestnum=num
    return largestnum
print(largest([23,12,56,4,534,7,8,765,43,454]))
