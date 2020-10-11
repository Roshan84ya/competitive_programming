"""

3**(13) = 3**(1101)2 = (3**8) * (3**4) * (3**1)

so we decompose the n --> binary(n) the we have only log(n) different places
see the example i wanted to calculate the power 8

procedure 1 :-
        3*3*3*3*3*3*3*3 = 3**8 --> 7 steps

        (((3**2)**2)**2) --> 3 steps

        3**1 = 2

        3**2 = (3**1)**2 = 9
        3**4 = (3**2)**2 = 81
        3**8 = ((3**4)**2) = 6581
        we will use this technique
"""
def power(n , powr):
    res = n
    result=1

    while (powr > 0):
        if (powr & 1):
            result*= res
        powr>>=1
        res*=res
    return result
#enter the interger
n = int(input())
#enter the power
powr = int(input())
print(power(n , powr))
