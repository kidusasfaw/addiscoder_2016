import sys

# function takes in list of coin denominations L and returns a SORTED list of
# the coins used to make change for n, using the fewest number of coins.
def makeChange(n, L):
    # implement this method

##################################
# DON'T EDIT CODE BELOW
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
