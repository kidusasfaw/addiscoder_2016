import sys

### students should implement fibonacci

def fibonacci(n):
    fib = [1, 1]
    count = 0
    while count < n-1:
    	last = fib[-2] + fib[-1]
    	last %= 1000000007
    	fib.append(last)
    	count += 1
    return fib[n]

### DO NOT EDIT ANY CODE BELOW THE LINE ###
n = int(sys.stdin.readline())
ans = fibonacci(n)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''