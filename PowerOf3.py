def is_It_POWEROF3(n):
    while n > 1 and n % 3 == 0:
        n = n / 3
        print(n)
    if n == 1:return True
    return False
print(is_It_POWEROF3((3**16) ))