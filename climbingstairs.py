def fibonachi(n):
    a =0
    b =1
    for i in range(n):
        a,b = b,a+b
    return b
print(fibonachi(4))