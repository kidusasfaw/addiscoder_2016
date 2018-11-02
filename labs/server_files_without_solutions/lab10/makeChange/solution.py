import sys

### students should implement makeChange
def makeChange(x):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
ans = makeChange(int(sys.stdin.readline()))
sys.stdout.write(str(ans[0]))
for z in ans[1:]:
    sys.stdout.write(' ' + str(z))
sys.stdout.flush()
print ''
