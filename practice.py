# m="abcdef"
# n=''
# # print(m[::-1])
# for i in range(len(m)-1,-1,-1):
#     n+=m[i]
# # print(n)
def prime(a):
# a=5
    if a<1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
print(prime(5))
