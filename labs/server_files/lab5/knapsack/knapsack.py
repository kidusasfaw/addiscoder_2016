import sys

def memKnapsack(L, n, at, mem):
    if at==len(L):
        return 0
    elif mem[n][at]!=-1:
        return mem[n][at]
    mem[n][at] = memKnapsack(L, n, at+1, mem)
    if L[at][0]<=n:
        mem[n][at] = max(mem[n][at], L[at][1] + memKnapsack(L, n-L[at][0], at+1, mem))
    return mem[n][at]    

def knapsack(n, L):
    mem = []
    for i in xrange(n+1):
        mem += [[-1]*len(L)]
    return memKnapsack(L, n, 0, mem)

n = int(sys.stdin.readline())
L = []
line = sys.stdin.readline().rstrip().split()
while line:
    int_list = [int(float(i)) for i in line]
    L.append(int_list)
    line = sys.stdin.readline().rstrip().split()
ans = knapsack(n, L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''