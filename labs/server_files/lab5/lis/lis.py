import sys

def memlis(L, last, at, mem):
    if at==len(L):
        return 0
    elif mem[last][at]!=-1:
        return mem[last][at]
    mem[last][at] = memlis(L, last, at+1, mem)
    if L[at]>L[last]:
        mem[last][at] = max(mem[last][at], 1 + memlis(L, at, at+1, mem))
    return mem[last][at]

def lis(L):
    mem = []
    for i in xrange(len(L)):
        mem += [[-1]*len(L)]
    answer = 0
    for i in xrange(len(L)):
        answer = max(answer, 1 + memlis(L, i, i+1, mem))
    return answer

line = sys.stdin.readline().rstrip().split()
L = [int(float(i)) for i in line]
ans = lis(L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''