"""
euclid throram it calculates the gcd( a, b) in log2(min(a,b)) time

"""

#recursive
def gcd(a , b):

    if (b==0):
        return a
    else:
        return gcd(b,a%b)


#iterative
def gcdi(a , b):
    while b:
        a ,b = b , a%b
    return a
    
a, b = map(int, input().split())

hcf = gcd(a,b)
lcm = (a*b)/hcf
hcf1 = gcdi(a,b)

print(hcf  , hcf1)
