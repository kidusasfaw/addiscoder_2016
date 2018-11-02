import sys

def convertScoreToGrade(n):
    if n >= 99:
        return 'A+'
    elif n >= 96:
        return 'A'
    elif n >= 93:
        return 'A-'
    elif n >= 90:
        return 'B+'
    elif n >= 87:
        return 'B'
    elif n >= 84:
        return 'B-'
    elif n >= 81:
        return 'C+'
    elif n >= 78:
        return 'C'
    elif n >= 75:
        return 'C-'
    elif n >= 70:
        return 'D'
    else:
        return 'F'

# INPUT OUTPUT CODE
inputLen = int(sys.stdin.readline().strip())
for i in range(inputLen):
    ans = convertScoreToGrade(int(sys.stdin.readline()))
    sys.stdout.write(str(ans) + "\n")
sys.stdout.flush()