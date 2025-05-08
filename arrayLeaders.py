def arrayLeaders(arr):
    result=[]
    rtmx=0
    for num in reversed(arr):
        if num >=rtmx:
            result.append(num)
            rtmx=num
    return result[::-1]

print(arrayLeaders([16, 17, 4, 3, 5, 2]))