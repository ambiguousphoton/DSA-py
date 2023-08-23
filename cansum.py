def cansum(target, nums, memory=None):
    if memory == None:
        memory = {}
    if target in memory: return memory[target]
    if target == 0: return True
    if target < 0: return False

    for number in nums:
        if number == 0: continue
        new_target = target - number
        if cansum(new_target, nums, memory):
            memory[target] = True
            return True
    
    memory[target] = False
    return False
 
print(cansum(7,[1,3])) # TRUE
print(cansum(7,[5,3,4,7,0])) # TRUE
print(cansum(7,[2,4])) # FALSE
print(cansum(8,[2,0,3,5])) # TRUE
print(cansum(300,[7,14])) # FALSE

