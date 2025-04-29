x = '34722641'       # 34724126
y=x
z=[]
for i in y:
    i=int(i)
    z.append(i)
# print(z) 
rt=-1
lt=-2
q=-1
c=-1
while z[lt]>=z[rt]:
    # print(z[q])
    q-=1
    rt-=1
    lt-=1
    
    if z[rt]>z[lt]:
        # print(rt)
        for i in range(-1,rt,-1):
            if z[i]%2==0 and z[i]<z[i-1]:
                z[rt-1],z[i]=z[i],z[rt-1]
            # print(z)
new=[]
for v in range(-1,rt-1,-1):
    new.append(z[v])
z=z[:rt]
new.sort()
# print(new)
# print(z)
p=z.extend(new)
print(z)
g=[]
for f in z:
    h=str(f)
    g.append(h)
    # print(type(h))
print(''.join(g))
    


    
    
    
    