def f(L, n):
    if n==0: return 1
    if len(L)==0: return 0
    ans = f(L[1:], n)
    if L[0] <= n:
        ans += f(L, n - L[0])
    return ans
    
