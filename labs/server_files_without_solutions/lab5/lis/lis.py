import sys

#This function takes in a list L of integers
def lis(L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
line = sys.stdin.readline().rstrip().split()
L = [int(float(i)) for i in line]
ans = lis(L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
