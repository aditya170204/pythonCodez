x="abcd efgh ijk lmn"

a= x.split()
z=[]
for i in a:
    reva=i[::-1]
    z.append(reva)
    # print(z)
    

print((" ".join(z)))