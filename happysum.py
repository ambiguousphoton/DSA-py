def happysum(n : int) :
    s_num = str(n)
    hsp = 0
    for i in s_num:
        hsp += int(i) ** 2
    if hsp == 4: return False
    if hsp == 1:return True
    return happysum(hsp)    
print(happysum(7))