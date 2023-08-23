def bestsum(target, nums, memory = None):
    if memory == None: memory = {}
    if target in memory: return memory[target]
    if target == 0 : return []
    if target < 0 : return None
    best_path = None
    for num in nums:
        if num == 0:
            continue
        nodes_target = target - num
                
        if bestsum(nodes_target, nums, memory) != None:
            path = bestsum(nodes_target, nums, memory).copy()
            path.append(num)
            if not best_path or len(best_path) > len(path):
                best_path = path
   
    if best_path: 
        memory[target] = best_path
        return best_path
    memory[target] = None
    return None

print(bestsum(7,[1,3])) # TRUE
print(bestsum(7,[5,4,3,7,0])) # TRUE
print(bestsum(7,[2,3])) # FALSE
print(bestsum(8,[2,0,3,5])) # TRUE
print(bestsum(100,[1,2,5,25]))
print(bestsum(8,[1,4,4]))

