import sys

#The input for this function is a list of numbers. The function should return the smallest number
def minElement(L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
list = map(int,sys.stdin.readline().split())
ans = minElement(list)
sys.stdout.write(str(ans))
print ''
