"""
here we are going to find the factors of the numbers

usually we were doing this in O(n) time i.e we were taking total n time
to find the factors that was the brute force approch but we can also do it in
O(sqrt(n)) time
how??

okay lets take an example of 20

all the factors of
20 = 1, 2, 4,  5, 10 , 20

see the above thing very carefully

now i'm re-writting the above thing

20 = 1*20  , 2*10 , 4*5 these are the only six factor
i.e

20 = [1 , 2, 4]*
     [20 , 10 , 5]

se here if we find the one root then we can easily find the other root
i.e by dividing the number by the current_root  we will get the other root

and now we can see for the 20 we only need to go till the 4 , and we can find all the root

now let's take another example
90 = 1 , 2, 3, 5, 6, 9, 10 , 15 ,18 , 30 , 45 , 90

for here also we only need to go till 9 then all the root are can be
obtained by dividing the first root by the number

90 --> 9
20 --> 4
for
n --> sqrt(n)

"""


import math
def all_factors(n):
    factors = []
    for i in range(1, round(math.sqrt(n))+1):
        if n%i==0:
            k = n//i
            #this case is for not containing the dubplicate value i.e when the both obtain roots are different
            
            if k!=i:
                factors.append(k)
            factors.append(i)
    factors.sort()
    return factors

print(*all_factors(20))
