"""
euclid says that gcd(a, b) = gcd( b , a%b)
prerequisite gcd_calculationLcm.py

in extended euclid we are also interested in  finding the coefficient of a, b i.e a*x + b*y = gcd(a,b) equation (i)

now by euclicid gcd(a, b) = gcd(b,a%b)

so we can say that
a*x1 + b*y1 = gcd(b , a%b) (the coefficient will change for the different value of a ,b as initially our a , b = a, b but when we applied extended euclid theoram we have
                            our a changes to b and our b changes to a%b so that result in change in our x and y too (common sense))
now i replace the a with b and b with a%b ( on comparision with equation i)

b*x1 + (a%b)*y1 = gcd(b , a%b)  = gcd( a, b)
but a%b = a- ceil(a/b)*b

b*x1 + (a - ceil(a/b)*b)*y1 = gcd

bx1 + ay1 - ceil(a/b)*b*y1 = gcd

b(x1 - ceil(a/b)*y1) + ay1 = gcd

a*y1 + b*(x1 - ceil(a/b)*y1) = gcd

now on comparing it with the equation 1 we can see that
x = y1
y = x1 - ceil(a/b)*y1

and here they are the coefficient that we were looking for



"""

def ExtendedEuclid(a , b):
    if b==0:
        return [1 , 0 , a]

    x1, y1 , gcd1 = ExtendedEuclid(b , a%b)
    gcd = gcd1
    x = y1
    y = x1 - (a//b)*y1
    
    return [x , y, gcd]
    
    

a , b = map(int, input().split())
x , y , gcd = ExtendedEuclid(a , b)

print(x, y , gcd)


