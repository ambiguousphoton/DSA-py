# o (logn)
def powerOftwo(n):
    while n>1:
        n = n/2
        print(n)
    if n == 1: return True
    return False

# o (1)
def pwr2(n):
    if n & (n - 1) == 0:
        return True
    return False

    # low,high = 0 ,n//2
    # while low<=high:
    #     middle  =  (low+high)//2
    #     if 2**middle == n:return True
    #     elif 2**middle<n:
    #         high = middle - 1
    #     else :
    #         low = middle + 1
    # return False
print(pwr2((2**32)+1))
512
256
128
64
32
16
4
2
1