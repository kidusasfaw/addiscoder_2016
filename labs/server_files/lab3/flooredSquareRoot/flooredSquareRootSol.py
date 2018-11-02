import sys

def flooredSquareRoot(n):
    i = 0
    while i ** 2 <= n:
        i += 1
    return i - 1

ans = flooredSquareRoot(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''