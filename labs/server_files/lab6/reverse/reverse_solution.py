import sys

### students should implement reverse
def reverse(L):
    if len(L)==0:
        return []
    return [L[len(L)-1]] + reverse(L[:len(L)-1])
        
### DO NOT EDIT ANY CODE BELOW THE LINE ###
list = sys.stdin.readline().split()
ans = reverse(list)
for z in ans[:-1]:
    sys.stdout.write(str(z) + ' ')
if len(ans)>0:
    sys.stdout.write(str(ans[-1]))
sys.stdout.flush()
print ''