import sys

# This function should take two inputs, n and intervals.
# 
# n           the index of the number we want to find
# intervals   a list of intervals [[a1,b2], ... ,[am,bm]]
#
# output:     the nth item of the union of the intervals
def calcNthSmallest(n, intervals):
    # student should implement this function
    

###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
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

