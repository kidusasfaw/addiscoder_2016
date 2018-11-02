import sys

### students should implement listOfWords
def listOfWords(s):
    cur = ''
    ret = []
    for c in s:
        if c==' ':
            ret += [cur]
            cur = ''
        else:
            cur += c
    ret += [cur]
    return ret

### DO NOT EDIT ANY CODE BELOW THE LINE ###  
words = listOfWords(raw_input())
print words





