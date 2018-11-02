### students should implement isPalindrome
def isPalindrome(n):
    s = str(n)
    for i in xrange(0,len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

### DO NOT EDIT ANY CODE BELOW THE LINE ###
n = int(raw_input())
print isPalindrome(n)
