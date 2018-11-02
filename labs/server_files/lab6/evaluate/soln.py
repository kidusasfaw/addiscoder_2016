import sys

# returns True if c represents a digit from '0' to '9'
# and False otherwise
def isDigit(c):
    return c>='0' and c<='9'

def isOperator(c):
    return c=='+' or c=='-' or c=='*'

# find the first prefix of expr which could be a valid expression
# return INVALID of no such prefix exists
def locateExpression(expr):
    if len(expr) == 0:
        return 'INVALID'
    elif isDigit(expr[0]):
        # try to build an integer expression as a prefix
        at = 1
        while at<len(expr) and isDigit(expr[at]):
            at += 1
        return expr[:at]
    elif expr[0] == '-':
        # try to build a negative integer expression as a prefix
        if len(expr) == 1:
            return 'INVALID'
        elif not isDigit(expr[1]):
            return 'INVALID'
        at = 2
        while at<len(expr) and isDigit(expr[at]):
            at += 1
        return expr[:at]
    elif expr[0] == '(':
        # find the matching parenthesis
        x = 1
        at = 1
        while at<len(expr) and x>0:
            if expr[at]=='(':
                x += 1
            elif expr[at]==')':
                x -= 1
            at += 1
        if x != 0:
            return 'INVALID'
        return expr[:at]
    else:
        return 'INVALID'

def evaluate(expr):
    if len(expr) == 0:
        return 'INVALID'
    elif expr[0] != '(':
        if locateExpression(expr) == expr:
            return int(expr)
        else:
            return 'INVALID'
    else:
        if len(expr) == 1:
            # if the first letter is '(', we at least need ')' at end
            return 'INVALID'
        elif expr[len(expr)-1] != ')':
            return 'INVALID'
        elif isOperator(expr[1]):
            # in this case we need to apply an OP to two exprs
            if (len(expr) < 7) or (expr[2] != ' '):
                # we need at least 7 characters for (, OP, two spaces, and two exprs
                return 'INVALID'
            expr1 = locateExpression(expr[3:])
            if expr1 == 'INVALID':
                return 'INVALID'
            elif len(expr1) >= len(expr)-4:
                # if expr1 is too long, there's no room left for expr2
                return 'INVALID'
            elif expr[3+len(expr1)] != ' ':
                # a space should separate the two expressions
                return 'INVALID'
            expr2 = locateExpression(expr[4+len(expr1):])
            if expr2 == 'INVALID':
                return 'INVALID'
            elif len(expr1)+len(expr2)+5 != len(expr):
                # expr should be (OP space expr1 space expr2)
                return 'INVALID'
            # evaluate the two expressions recursively
            A = evaluate(expr1)
            B = evaluate(expr2)
            if (A=='INVALID') or (B=='INVALID'):
                return 'INVALID'
            elif expr[1] == '+':
                return A + B
            elif expr[1] == '-':
                return A - B
            else:
                return A * B
        else:
            return evaluate(expr[1:len(expr)-1])


### DO NOT EDIT ANY CODE BELOW THE LINE ###
expr = sys.stdin.readline().strip()
ans = evaluate(expr)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
