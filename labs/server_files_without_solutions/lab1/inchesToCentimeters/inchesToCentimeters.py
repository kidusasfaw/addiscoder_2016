import sys

def inchesToCentimeters(x):
    # student should implement this function and return the correct value

###########################################
# INPUT OUTPUT CODE. DO NOT EDIT WHAT IS WRITTEN BELOW.
ans = inchesToCentimeters(float(sys.stdin.readline()))
# prevent precision errors by rounding
sys.stdout.write(str(round(ans, 3)))
sys.stdout.flush()
print("")
