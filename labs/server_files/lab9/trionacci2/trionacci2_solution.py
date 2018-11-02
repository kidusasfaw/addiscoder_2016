import sys

### students should implement trionacci
def matrixMultiply(A,B):
	n = len(A)
	m = len(A[0])
	p = len(B[0])
	C = []
	for i in xrange(n):
		C += [[0]*p]
	for i in xrange(n):
		for j in xrange(p):
			for k in xrange(m):
				C[i][j] += A[i][k]*B[k][j]
				# mod by 1000000007
				C[i][j] %= 1000000007
	return C

def matrixPower(A,n):
	if n == 0:
		#	return the identity matrix I, which has all 1s on the diagonal
		#	and 0s everywhere else. I*T = T for any matrix T
		I = []
		for i in xrange(len(A)):
			I += [[0]*len(A)]
		for i in xrange(len(A)):
			I[i][i] = 1
		return I
	B = matrixPower(A,n/2)
	B = matrixMultiply(B,B)
	if n%2 == 1:
		B = matrixMultiply(B,A)
	return B

def trionacci(n):
	A = [[1,1,1],[1,0,0],[0,1,0]]
	B = matrixMultiply(matrixPower(A,n),[[1],[1],[1]])
	return B[2][0]


### DO NOT EDIT ANY CODE BELOW THE LINE ###
#list = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
ans = trionacci(n)
sys.stdout.write(str(ans))
print ''
