import sys

### students should implement fibonacci


def fibonacci(n):
    if n <= 1: return 1
    a = 1
    b = 1
    while n > 1:
        c = a + b
        a = b
        b = c
        n = n - 1
    return b


### DO NOT EDIT ANY CODE BELOW THE LINE ###
n = int(sys.stdin.readline())
ans = fibonacci(n)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
