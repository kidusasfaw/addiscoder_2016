import sys

# This function takes in a list of lists L such that each L[i] is a list of size 3, representing in order the length, width, and height of a single box
def boxes(L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
L = []
line = sys.stdin.readline().rstrip().split()
while line:
    int_list = [int(float(i)) for i in line]
    L.append(int_list)
    line = sys.stdin.readline().rstrip().split()
ans = boxes(L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
