def rowWithMax1s( arr):
        # code here
        dis={}
        valu=0
        idx=None
        for i in range(len(arr)):
            for x in arr[i]:
                if x==1:
                    dis[i]=dis.get(i,0)+1
        for key,val in dis.items():
            if valu<val:
                valu=val
                idx=key
        return idx

print(rowWithMax1s([[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]))