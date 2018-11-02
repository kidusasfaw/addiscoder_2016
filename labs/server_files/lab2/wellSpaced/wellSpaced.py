### students should implement wellSpaced
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

def wellSpaced(n):

    # Calculate floor(sqrt(n))
    squareRoot = 0
    while squareRoot*squareRoot <= n:
        squareRoot += 1
    squareRoot -= 1

    # Get the list of primes up to the square root
    primeList = listOfPrimes(squareRoot)
    
    # Add on the very next prime after the square root
    lastPrime = primeList[len(primeList)-1] + 1
    while not isPrime(lastPrime):
        lastPrime += 1

    primeList += [lastPrime]

    # Check for adjacent prime divisors
    for i in xrange(len(primeList)-1):
        if n%primeList[i]==0 and n%primeList[i+1]==0:
            return False
    return True


### DO NOT EDIT ANY CODE BELOW THE LINE ###
n = int(raw_input())
print wellSpaced(n)
