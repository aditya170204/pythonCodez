def countFreq( arr, target):
        
        count = 0
        for num in arr:
            if num==target:
                count+=1
        return count
print(countFreq([0,2,0,30,4,0,50,60,70,7,0,70,70,80,90,0,60,6,0,0,6,0,6,0,6,0,0,6],6))