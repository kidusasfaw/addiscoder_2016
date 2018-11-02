import sys

# slow implementation, without using binary search
def calcNthSmallest2(n, intervals):
    for L in intervals:
        for x in xrange(L[0], L[1]+1):
            first = firstTime(x, intervals)
            last = lastTime(x, intervals)
            if first<=n and n<=last:
                return x























# compute the index of the first time x appears in the union of intervals
def firstTime(x, intervals):
    answer = 0
    for L in intervals:
        if x > L[1]:
            answer += L[1] - L[0] + 1
        elif x > L[0]:
            answer += x - L[0]
    return answer

# compute the index of the last time x appears in the union of intervals
def lastTime(x, intervals):
    answer = 0
    for L in intervals:
        if x >= L[1]:
            answer += L[1] - L[0] + 1
        elif x >= L[0]:
            answer += x - L[0] + 1
    return answer-1

# assumes the item occurring at position n in the union of intervals is in [a,b]
# and binary searches to find which element in [a,b] it is. If the assumption
# is wrong, return [False, '']. Otherwise return [True, x], where x is at 
# position n
def binarySearch(a, b, n, intervals):
    if a>b:
        return [False, '']
    mid = (a+b)/2
    first = firstTime(mid, intervals)
    last = lastTime(mid, intervals)

    if first<=n and n<=last:
        return [True, mid]
    elif first > n:
        return binarySearch(a, mid-1, n, intervals)
    else:
        return binarySearch(mid+1, b, n, intervals)

def calcNthSmallest(n, intervals):
    # The answer has to be in one of the intervals, so try them all in a for loop.
    for L in intervals:
        answer = binarySearch(L[0], L[1], n, intervals)
        if answer[0]:
            return answer[1]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
intervals = []
for i in range(M):
    read = sys.stdin.readline().split(" ")
    interval = [int(read[0]), int(read[1])]
    intervals.append(interval)

ans = calcNthSmallest(N, intervals)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
