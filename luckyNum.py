def luckynum(name):
    val=0
    for i,lett in enumerate(name):
    
        asciiLett=ord(lett)
        
        val=val+(asciiLett*(i+1))
    if len(name)%2!=0 or val%2!=0:
        return f"{val} is the lucky no for {name}"
print(luckynum('ADITYA'))    