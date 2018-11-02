import sys

#This function takes in two inputs. Integer n represents the maximum volume of the knapsack. L is a list of lists such that each L[i] represents the volume and value of item i
def knapsack(n, L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
n = int(sys.stdin.readline())
L = []
line = sys.stdin.readline().rstrip().split()
while line:
    int_list = [int(float(i)) for i in line]
    L.append(int_list)
    line = sys.stdin.readline().rstrip().split()
ans = knapsack(n, L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
