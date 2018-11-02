import sys

### students should implement reverse
def minElement(L):
	if len(L)==1:
		return L[0]
	return min(L[0], minElement(L[1:]))
        
### DO NOT EDIT ANY CODE BELOW THE LINE ###
list = map(int,sys.stdin.readline().split())
ans = minElement(list)
sys.stdout.write(str(ans))
print ''