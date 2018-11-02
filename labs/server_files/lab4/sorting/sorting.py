import sys

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
L = []
for i in range(n):
    L.append(int(inputLine[i + 1]))
L = mergeSort(L)
for i in range(n - 1):
    sys.stdout.write(str(L[i]) + " ")
sys.stdout.write(str(L[n - 1]))
