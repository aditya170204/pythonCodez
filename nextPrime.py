def pmc(m):
        if m<2:
            return False
        for i in range(2,m):
            if m%i==0:
                return False
        return True
def nextPrime(n):
    
    
    n+=1
    while True:
        if pmc(n):
            return n
        n+=1
    
print(nextPrime(16))