### students should implement isPrime and listOfPrimes
def isPrime(n):
    if n<2:
        return False
    for x in xrange(2,n):
        if x*x > n:
            break
        if n%x==0:
            return False
    return True

def listOfPrimes(n):
    ret = []
    for x in xrange(2,n+1):
        if isPrime(x):
            ret += [x]
    return ret

### DO NOT EDIT ANY CODE BELOW THE LINE ###
n = int(raw_input())
print listOfPrimes(n)
