import sys

# the input for this function is the image in the form of a list of lists. 
# the output is an integer which is the area of the largest object in the image.
def largestObjInImage(image):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
dim = sys.stdin.readline().strip().split(' ')
n = int(dim[0])
m = int(dim[1])
image = []
for i in xrange(n):
	image += [sys.stdin.readline().strip().split(' ')]
ans = largestObjInImage(image)
sys.stdout.write(str(ans))
print ''

