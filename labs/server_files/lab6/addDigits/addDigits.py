import sys

def addDigits(n):
    if n==0:
        return 0
    return (n%10) + addDigits(n/10)

ans = addDigits(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''