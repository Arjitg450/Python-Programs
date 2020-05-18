#gcd  = the maximum divisor of two numbers.
#ex: gcd of 6 and 12 is 6, gcd of 27 and 18 is 9.

def gcd(a, b):
    if a==b:
        return a
    elif a==0:
        return b
    elif b==0:
        return a
    elif a%b==0:
        return b
    elif b%a==0:
        return a
    
    
    elif a>b:
        return gcd(a%b,b)
            
    else:
        return gcd(a,b%a)
    


print(gcd(100,24))
