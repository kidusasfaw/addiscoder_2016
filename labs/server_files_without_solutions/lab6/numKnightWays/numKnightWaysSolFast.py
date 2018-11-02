import sys

# This function takes as input two coordinates x and y, which the knight
# must eventually reach, and a list of pairs L. L[i] should be a list of
# length 2, representing a possible knight move--for example, if L[i] is
# [4, 5], the knight can move four units horizontally and five vertically
# in a single move.
def numKnightWays(x, y, L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
x, y, length = tuple(map(int, sys.stdin.readline().split()))
L = [map(int, sys.stdin.readline().split()) for i in range(length)]
ans = numKnightWays(x, y, L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
