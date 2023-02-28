def numberofOnebits(num):
    return num
    nm = str(int(num))
    sm = 0
    for i in nm:
        sm += int(i)
    return sm
print(numberofOnebits())

