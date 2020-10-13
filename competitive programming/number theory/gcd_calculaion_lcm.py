"""
euclid theoram
it calculates the gcd of a numeber in log2(min(a,b)) << min(a , b) 
"""

def gcd(a , b):

    if (b==0):
        return a
    else:
        return gcd(b,a%b);
    
a, b = map(int, input().split())

hcf = gcd(a,b)
lcm = (a*b)/hcf
