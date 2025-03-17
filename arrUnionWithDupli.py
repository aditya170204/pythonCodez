def union(a,b):
    a.extend(b)
    c=set(a)
    d=list(c)
    return d, len(d)



print(union([1, 2, 3, 4, 5],[1, 2, 3]))