def factorial(n):
    if (n <= 1): return 1  
    return n * factorial(n - 1)

def calculate(n , k):
    return factorial(n)//(factorial(k)*factorial(n - k))

print(calculate(4,2))
def Pascalstriangle(num):
    lst = []
    lst2 = []
    
    for i in range(num):
        for j in range(i+1):
            lst2.append(calculate(i,j)) 
        lst.append(lst2)
        lst2 = []
    return lst

print(Pascalstriangle(5))