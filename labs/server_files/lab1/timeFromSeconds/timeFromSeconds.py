import sys

def timeFromSeconds(x):
    seconds = x%60
    minutes = int(x/60)%60
    hour = int(x/60/60)
    return str(hour) + ':' + str(minutes) + ':' + str(seconds)

# INPUT OUTPUT CODE
ans = timeFromSeconds(int(sys.stdin.readline()))
sys.stdout.write(str(ans))
sys.stdout.flush()
print("")

'''
# RANDOM TEST GENERATION CODE
import random
for i in range(10):
    s = int(random.random()*60*60*24)
    print(str(s) + " (" + timeFromSeconds(s) + ")")
'''