def grid_traveler(n, m, memory = {}): # n rows, m col 
    key = f'{n},{m}'
    key_reverse = f'{m},{n}'
    if key in memory:
        return memory[key]
    elif key_reverse in memory:
        return memory[key_reverse]

    if n == 1 and m == 1:
        return 1
    if not n or not m:
        return 0
    
    memory[key] = grid_traveler(n - 1, m, memory) + grid_traveler(n ,m - 1, memory)
    return memory[key]
print(grid_traveler(18,18))