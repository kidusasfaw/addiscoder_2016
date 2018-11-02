import sys

### students should implement makeChange
def makeChange(x):
    ret = []
    denoms = [25, 10, 5, 1]
    pos = 0
    while pos < 4:
        if denoms[pos] > x:
            pos += 1
            continue
        else:
            ret += [denoms[pos]]
            x -= denoms[pos]
    return ret
        
### DO NOT EDIT ANY CODE BELOW THE LINE ###
ans = makeChange(int(sys.stdin.readline()))
sys.stdout.write(str(ans[0]))
for z in ans[1:]:
    sys.stdout.write(' ' + str(z))
sys.stdout.flush()
print ''
