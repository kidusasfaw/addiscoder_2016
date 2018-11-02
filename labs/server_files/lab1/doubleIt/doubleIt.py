import sys

def doubleIt(x):
    return x + x

# INPUT OUTPUT CODE
inputCode = sys.stdin.readline().strip()
inputObj = []
# if string, just read
if inputCode == 'S':
    inputObj = sys.stdin.readline().strip("\n")
# if list, read lenght and unpack into list
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