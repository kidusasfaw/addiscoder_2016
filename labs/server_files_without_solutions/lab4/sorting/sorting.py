import sys

# function takes in list L of integers, should return sorted list of integers
def mergeSort(L):
    # implement this function

##############################################
# DONT EDIT CODE BELOW
inputLine = sys.stdin.readline().strip().split(" ")
n = int(inputLine[0])
L = []
for i in range(n):
    L.append(int(inputLine[i + 1]))
L = mergeSort(L)
for i in range(n - 1):
    sys.stdout.write(str(L[i]) + " ")
sys.stdout.write(str(L[n - 1]))
