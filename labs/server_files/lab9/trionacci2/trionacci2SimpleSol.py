import sys

### students should implement trionacci

def trionacci(n):
        if n <= 2: return 1
        a = 1
        b = 1
        c = 1
        while n > 2:
                d = a+b+c
                a = b
                b = c
                c = d
                n = n - 1
        return c


### DO NOT EDIT ANY CODE BELOW THE LINE ###
#list = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
ans = trionacci(n)
sys.stdout.write(str(ans))
print ''
