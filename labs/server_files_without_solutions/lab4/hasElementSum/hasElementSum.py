import sys

# function tests if there exist two elements in list L of integers that sum to a
# given integer n, if so, returns the two integers, else, returns False.
def hasElementSum(n, L):
    # implement this

#####################################
# DON'T EDIT CODE BELOW
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
