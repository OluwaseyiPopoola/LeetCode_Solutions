x, a, m= list(map(int, input().split()))




def exp(x, a, m): 
    if a == 0:
        return 1 % m
    
    if a == 1:
        return x % m

    if a % 2 == 0:
        rt = exp(x, a//2, m) % m
        return (rt*rt) % m

    else:
        return ((a % m) * (exp(x, a - 1, m) % m)) % m

def iter_exp(x, a, m):
    res = 1

    while a > 0:
        if (a & 1):
            res = (res * x) % m
        res = (res % m) * (res % m)
        a >> 1
        
    return res
 
def fibExp():
    start = 
        

print(exp(x, a, m))

