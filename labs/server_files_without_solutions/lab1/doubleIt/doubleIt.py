import sys

def doubleIt(x):
    # student should implement this function and return the correct value

###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
inputCode = sys.stdin.readline().strip()
inputObj = []
# if string, just read
if inputCode == 'S':
    inputObj = sys.stdin.readline().strip("\n")
# if list, read length and unpack into list
elif inputCode == 'L':
    listLen = int(sys.stdin.readline())
    for i in range(listLen):
        inputObj.append(sys.stdin.readline().strip("\n"))
# fail with wrong format entered
else:
    sys.stderr.write("Invalid input format!\n")
    sys.exit(1)

ans = doubleIt(inputObj)

if inputCode == 'S':
    sys.stdout.write(str(ans) + "\n")
# unpack list
elif inputCode == 'L':
    for x in ans:
        sys.stdout.write(str(x) + "\n")
sys.stdout.flush()
