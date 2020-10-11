#checking whether a number is prime or not


"""
this is most probably based on finding the factor check find_factor.py

here we know that for any number n it's factor will only exist in the range of
sqrt(n) so if any number is not divisible by the number till it's square root
then the number will be the prime number
space complexity is O(1)
time complexity is O(sqrt(n))
"""
def is_prime(n):
    #no number smaller than 2 is prime 
    if n<2:
        return False
    

    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1
    return True
