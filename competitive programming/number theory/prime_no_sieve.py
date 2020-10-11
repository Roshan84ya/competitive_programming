"""
here we are using the formula i.e if we have n numbers then
1, 2, 3, 4, 5, ........., n

--> 1 is not prime
--> 2 is prime then all the multiple of 2 is not the prime
--> 3 is prime then all the multiple of 3 is not the prime
--> similarly for 5 ans so on


"""

###############################################################################

#finding all the prime number from 1.......n
"""
here in the prime we are having all the prime number indexes = True and other have false
the space complexity is O(n) and
time complexity is O(n*(log(logn)))
"""

def nprime(n):
    
    prime = [True]*n
    prime[0] = False
    prime[1]=False
    for i in range(2, n):
        if prime[i]:
            for j in range(i*i , n, i):
                prime[j]=False

    i=10
    j=0
    while i:
        if prime[j]:
            print(j , end = " ")
            i-=1
        j+=1
    print()

    
n= 10**5
n+=1
nprime(n)








    
    
