import sys

### students should implement nextPalindrome
def reverse(s):
    t = ''
    for i in xrange(len(s)):
        t += s[len(s) - i - 1]
    return t

def nextPalindrome(n):
    if n<9:
        return n+1
    elif n==9:
        return 11
    s = str(n)
    t = s[0:len(s)/2]
    trev = reverse(t)
    if int(t + trev) > n:
        return int(t + trev)
    if len(s)%2==1 and int(t + s[len(s)/2] + trev)>n:
        return int(t + s[len(s)/2] + trev)
    if len(s)%2==1 and s[len(s)/2]!='9': 
        return int(t + str(int(s[len(s)/2]) + 1) + trev)
    else:
        tInc = str(int(t)+1)
        tIncRev = reverse(tInc)
        if len(tInc)==len(t):
            if len(s)%2==0:
                return int(tInc + tIncRev)
            else:
                return int(tInc + '0' + tIncRev)
        else:
            ret = '1'
            for i in xrange(len(s)-1):
                ret += '0'
            ret += '1'
            return int(ret)

### DO NOT EDIT ANY CODE BELOW THE LINE ###
ans = nextPalindrome(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
