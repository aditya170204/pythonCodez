def armstrongNo(num):

    if num<0:
        return False
    li=list(str(num))

    sumi=0
    for i in li:
        i=int(i)
        sumi+=i**len(li)
        
    if num==sumi:
        return True
    else:
        return False

print(armstrongNo(371))