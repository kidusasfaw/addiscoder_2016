import sys

def convertScoreToGrade(n):
    # student should implement this function

###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
inputLen = int(sys.stdin.readline().strip())
for i in range(inputLen):
    ans = convertScoreToGrade(int(sys.stdin.readline()))
    sys.stdout.write(str(ans) + "\n")
sys.stdout.flush()
