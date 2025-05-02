def findIndex(str):
        
        n=len(str)
        opn=[0] * (n + 1)
        close= [0] * (n + 1)
        for i in range(n):
            opn[i + 1] = opn[i] + (1 if str[i] == '(' else 0)
            
        for i in range(n - 1, -1, -1):
            close[i] = close[i + 1] + (1 if str[i] == ')' else 0)
        
        for i in range(n + 1):
            if opn[i] == close[i]:
                return i
            
print(findIndex("(())))("))