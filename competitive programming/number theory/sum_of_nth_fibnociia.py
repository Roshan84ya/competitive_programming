"""
fomula used 
sum of 1....nth fibnoccia is = fn+2 -1
f1+f2+f3+f4+.....+f5 = fn+2 -1

so to calculate this we have to find the nth term of fibnoccia series

but here we wanted to find it in log(N) time because our costrainsts ate
so high

this will done =

(fn-1 , fn) = (f n-2 , fn-1) *([0 1]
                               [1,1])
--> (fn , fn+1) = (f0 , f1) * (p**n)

now all we need is to calculate the powe of the p to the n
and we know this how to calculate the power n in logn time

i.e
go and see power_n_log(n)



"""

def mul(a,b):
    mod = 10**9 +7
    if len(a)==len(b):
        a[0][0]%=mod
        a[1][0]%=mod
        a[0][1]%=mod
        a[1][1]%=mod
        b[0][0]%=mod
        b[0][1]%=mod
        b[1][0]%=mod
        b[1][1]%=mod
        x1 = ((a[0][0]*b[0][0]) + (a[0][1]*b[1][0]))%mod
        x2 = ((a[0][0]*b[0][1]) + (a[0][1]*b[1][1]))%mod
        y1 = ((a[1][0]*b[0][0]) + (a[1][1]*b[1][0]))%mod
        y2 = ((a[1][0]*b[0][1]) + (a[1][1]*b[1][1]))%mod
        arr= [[x1,x2],[y1,y2]]
    else:
        b[0][0]%=mod
        b[0][1]%=mod
        b[1][0]%=mod
        b[1][1]%=mod
        a[0][0]%=mod
        a[0][1]%=mod
        x1 = ((a[0][0]*b[0][0]) + (a[0][1]*b[1][0]))%mod
        x2 = ((a[0][0]*b[0][1]) + (a[0][1]*b[1][1]))%mod
        arr=[[x1 , x2]]
    return arr
        
def power(p,n):
    res = [
            [1,0],
            [0,1],
            ]
    
    while n>0:
        if (n&1):
            res= mul(res , p)
        p=mul(p,p)
        n>>=1
    return res
            
            
def term(n):
    mod = 10**9 +7
    p=[
        [0,1],
        [1,1],
        ]
    f=[[0,1]]
    k = mul(f,power(p,n))
    tn = k[0][0]
    
    return (tn-1 +mod)%mod
 
mod = 10**9 +7
for _ in range(int(input())):
    a, b =map(int, input().split())
    print((term(b+2) - term(a+1) + mod)%mod)
