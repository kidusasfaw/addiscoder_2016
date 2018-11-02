import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

ans = factorial(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''


