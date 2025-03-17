def switchCase(choice, arr):
        if choice==1:
            return 3.14159265359*(arr[0]*arr[0])    #will take the arr[0] as radius and return area of circle
        elif choice==2:
             return arr[0]*arr[1]   
             
        # will take the arr[0] and arr[1] as length and breadth and return area of circle
        
        else:
            return -1

print(switchCase(1,[5,2]))
print(switchCase(2,[5,2]))