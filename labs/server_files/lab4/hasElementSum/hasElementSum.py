import sys

def binarySearch(n, a, b, L):
    if a > b:
        return False
    mid = (a + b)/2
    if L[mid] == n:
        return True
    elif L[mid] > n:
        return binarySearch(n, a, b-1, L)
    else:
        return binarySearch(n, mid + 1, b, L)

def hasElementSum(n, L):
    L = mergeSort(L)
    for i in xrange(len(L)):
        v = L[i]
        if v+v==n:
            if (i > 0 and L[i - 1] == v) or (i + 1 < len(L) and L[i + 1] == v):
                return [v, v]
            else:
                continue
        elif binarySearch(n-v, 0, len(L)-1, L):
            return [v, n-v]
    return False

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

inputLine = sys.stdin.readline().strip().split(" ")
n = int(inputLine[0])
length = inputLine[1]
L = []
for i in range(int(length)):
    L.append(int(inputLine[i + 2]))

output = hasElementSum(n, L)
if (output == False):
    sys.stdout.write(str(False))
else:
    sys.stdout.write(str(output[0]) + " " + str(output[1]))
