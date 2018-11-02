import sys

# this function takes a list as input and outputs the list in reversed order as output
def reverse(L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
list = sys.stdin.readline().split()
ans = reverse(list)
for z in ans[:-1]:
    sys.stdout.write(str(z) + ' ')
if len(ans)>0:
    sys.stdout.write(str(ans[-1]))
sys.stdout.flush()
print ''
