import sys

def memMakeChange(n, L, mem):
    if n == 0:
        return []
    elif mem[n] != -1:
        return mem[n]
    mem[n] = []
    length = n + 1
    for coin in L:
        if coin <= n:
            val = memMakeChange(n - coin, L, mem)
            if 1 + len(val) < length:
                mem[n] = val + [coin]
                length = len(mem[n])
    return mem[n]

def mergeSort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def makeChange(n, L):
    mem = []
    for i in xrange(n + 1):
        mem += [-1]
    return mergeSort(memMakeChange(n, L, mem))

inputLine = sys.stdin.readline().strip().split(" ")
n = int(inputLine[0])
length = int(inputLine[1])
L = []
for i in range(length):
    L.append(int(inputLine[i + 2]))
soln = makeChange(n, L)
if len(soln) == 0:
    sys.stdout.write(False)
else:
    for i in range(len(soln) - 1):
        sys.stdout.write(str(soln[i]) + " ")
    sys.stdout.write(str(soln[len(soln) - 1]))
