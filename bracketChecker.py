def isValidBracket( s):
        
        arr=[]
        bracket={')':'(',']':'[','}':'{'}
        for char in s:
            if char in bracket.values():
                arr.append(char)
            elif char in bracket:
                if not arr or arr[-1] != bracket[char]:
                    return False
                arr.pop()
            else:
                return False
        return not arr


print(isValidBracket("[{()}]"))
print(isValidBracket("[()()]{}"))
print(isValidBracket("([]"))