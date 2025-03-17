# a=[0,1,2,3,4,5,6,7,8,9]
# print(a[1:3])
# a[::2]
# print(a)




# def moveZeroToEnd(arr):
#     arr1=[]
#     arr2=[]
#     for num in arr:
#     	if num==0:
#     	    arr2.add(num)
#     	else:
			
#     	    arr1.add(num)
    	        
#     	arr1.append(arr2)
#     	return arr1
            

# def pushZerosToEnd(self,arr):
    
#     arr1=[]
#     arr2=[]
#     for num in arr:
#     	if num==0:
#     	    arr2.append(num)
#     	else:
#     	    arr1.append(num)
    	        
#     return arr1.extend(arr2)


def pushZerosToEnd(arr):
    n= len(arr)
    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
print(pushZerosToEnd([0,2,0,30,4,0,50,60,70,7,0,70,70,80,90,0,60,6,0,0,6,0,6,0,6,0,0,6]))
