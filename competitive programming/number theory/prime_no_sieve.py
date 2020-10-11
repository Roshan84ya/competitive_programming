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
import math

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




##############################################################################

#2nd version

"""
time complexity will not imact much in this case too
n(log(log(sqrt(n)))
and space will O(n)

"""

def nprime(n):
    
    prime = [True]*n
    prime[0] = False
    prime[1]=False
    for i in range(2, round(math.sqrt(n))):
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


###############################################################################

#3rd version when n is very big more than 10**8

"""
then in this case we cannot allcoate more memory than 10**8 as it may cause memory limit
exceed so how can we the number that are greater than it

there is another property of the prime number i.e when a number is not divisible
by the prime number (all the smaller prime number then that number is also a prime)
number

"""
def big_is_prime(arr , n):

    for i in arr:
        if i*i <= n:
            if n%i == 0:
                return False
    return True

    

def nprime(n):
    
    prime = [True]*n
    prime[0] = False
    prime[1]=False
    for i in range(2, round(math.sqrt(n))):
        if prime[i]:
            for j in range(i*i , n, i):
                prime[j]=False
    prime_number = []

    for i in range(1,n+1):
        if is_prime[i]:
            prime_number.append(i)
    
    return prime_number
n = int(input())

prime_num = nprime(n)
print(big_is_prime(prime_num , n))








    
    
