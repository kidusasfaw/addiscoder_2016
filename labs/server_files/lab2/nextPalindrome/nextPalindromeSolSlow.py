import sys

### students should implement nextPalindrome
def isPalindrome(n):
    s = str(n)
    for i in xrange(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def nextPalindrome(n):
    x = n+1
    while not isPalindrome(x):
        x += 1
    return x

### DO NOT EDIT ANY CODE BELOW THE LINE ###
ans = nextPalindrome(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''