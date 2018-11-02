import sys

def memoize(L, at, last, mem):
    if at==len(L):
        return 0
    elif mem[at][last] != -1:
        return mem[at][last]
    mem[at][last] = memoize(L, at+1, last, mem)
    if L[at][0]<L[last][0] and L[at][1]<L[last][1]:
        mem[at][last] = max(mem[at][last], L[at][2] + memoize(L, at+1, at, mem))
    return mem[at][last]

def boxes(L):
    T = []
    # put all 6 rotations of each box in a list
    for box in L:
        a1 = [box[0]*box[1], box[0], box[1], box[2]]
        a2 = [box[0]*box[1], box[1], box[0], box[2]]
        b1 = [box[0]*box[2], box[0], box[2], box[1]]
        b2 = [box[0]*box[2], box[2], box[0], box[1]]
        c1 = [box[1]*box[2], box[1], box[2], box[0]]
        c2 = [box[1]*box[2], box[2], box[1], box[0]]
        T += [a1, a2, b1, b2, c1, c2]
    # sort the list in decreasing order of base area
    T.sort()
    T.reverse()
    L = []
    for x in T:
        L += [[x[1], x[2], x[3]]]
    mem = []
    for i in xrange(len(L)):
        mem += [[-1]*len(L)]
    ans = 0
    # try all possibilities for the box at the very bottom and
    # take the best one
    for i in xrange(len(L)):
        ans = max(ans, L[i][2] + memoize(L, i+1, i, mem))
    return ans

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