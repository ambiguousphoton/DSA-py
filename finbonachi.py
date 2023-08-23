def fibonachi(n, memory = {}):    
    if n in memory:
        return memory[n]
    if n == 0:
        memory[0] = 0
        return 0
    if n <= 2:
        memory[n] = 1
        return 1
    memory[n] = fibonachi(n-1, memory) + fibonachi(n-2, memory) 
    return memory[n]

print(fibonachi(50))