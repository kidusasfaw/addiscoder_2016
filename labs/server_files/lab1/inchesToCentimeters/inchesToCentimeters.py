import sys

def inchesToCentimeters(x):
    return x * 2.54

# INPUT OUTPUT CODE
ans = inchesToCentimeters(float(sys.stdin.readline()))
# prevent precision errors by rounding
sys.stdout.write(str(round(ans, 3)))
sys.stdout.flush()
print("")