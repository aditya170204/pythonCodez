arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
common=None
arr=sorted(arr)
print(arr)
idx=0
pre=''
ok1=arr[0]
ok2=arr[len(arr)-1]
for i in range(len(arr[0])):
    if ok1[i]==ok2[i]:
        pre=pre+ok1[i]
    else:
        break
            
print(pre)
        