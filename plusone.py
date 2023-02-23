def plusone(lst):
    strng = ""
    for i in lst:
        strng += str(i)
    strng = str(int(strng) + 1)
    lst  = []
    for i in strng:
        lst.append(int(i))
    return lst
    
print(plusone([1,2,9]))