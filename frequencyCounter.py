def frequencyCounter( arr):
    
        n=len(arr)
        arr1=[]
        for i in range(1,n+1):
            count=0
            for num in arr:
                if num ==i:
                    count+=1
               
            arr1.append(count)
        return arr1
print(frequencyCounter([0,2,0,3,4,0,5,6,7,7,0,7,7,8,9,0,6,6,0,0,6,0,6,0,6,0,0,6]))



# =======================================+++++++++++++++++=========================

def frequencyCount( arr):
        
        n=len(arr)
        arr1={}
        for num in arr:
            if  num>=1 and num<= n:   
                arr1[num]= arr1.get(num,0)+1
                
                
        return [arr1.get(i,0) for i in range(1,n+1)]

print(frequencyCount([0,2,0,3,4,0,5,6,7,7,0,7,7,8,9,0,6,6,0,0,6,0,6,0,6,0,0,6]))