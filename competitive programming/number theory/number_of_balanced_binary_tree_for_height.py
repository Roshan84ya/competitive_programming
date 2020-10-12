"""
we are having the question of finding the total number of binary tree of height
h

se if we will take a general case then we can se for a height h
we can have 3 condition

case 1 : -   H
            / \
         H-1  H-1

case2 :-     H
            / \
         H-2  H-1

case 3: -    H
            / \
         H-1  H-2

a tree is said to be balanced binary tree if it has it's height of left subtree - height of
right subtree <= 1

Hl - Hr < = 1
so for this case we can have only above mention three steps so now for case one
we can have x*x = toal number of case where x= total number of h-1 subtree on the
left and right
similarly fot case 2 and case 3 we can have y*x and x*y respectively

so our answer will be :- x**2 + 2*x*y 
"""

#space complexity = h
#time complexity = h here we are using iterative approch as it runs faster than
# recursive
mod = 10**9 + 7
h= int(input())

dp = [1 , 1]
sum1 = [ 1, 2]
# the index of dp will show the height of the tree and it's corresponding value will
#show the number of balanced binary tree for that index
for i in range(2, h+1):
    #x = h-1 , y = h-2
    dp.append( (dp[i-1]*dp[i-1])%mod + (2*dp[i-1]*dp[i-2])%mod  + mod)%mod
print(dp[h])

#########################################################################
#recursive approach
#time complexith = 2**h
#space complexity = 2**h
def bst(h):
    if h==0 or h==1:
        return 1
    x = bst(h-1)
    y = bst(h-2)

    ans = x*x + 2*x*y
    return ans

print(bst(int(input())))
