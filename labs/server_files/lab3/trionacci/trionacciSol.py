import sys

def trionacci(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return trionacci(n-1) + trionacci(n-2) + trionacci(n-3)

ans = trionacci(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
