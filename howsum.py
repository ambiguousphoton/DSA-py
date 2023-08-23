def howsum(target, nums, memory = None):
    if memory == None:
        memory = {}
    if target in memory: return memory[target]
    if target == 0 : return []
    if target < 0 : return None
    for num in nums:
        if num == 0:
            continue
        childs_target = target - num
        sum_path = howsum(childs_target, nums, memory)
        memory[target] = sum_path

        if sum_path != None:
            sum_path.append(num)
            return sum_path
    return None


print(howsum(7,[1,3])) # TRUE
print(howsum(8,[5,4,7,0])) # TRUE
print(howsum(7,[2,4])) # FALSE
print(howsum(8,[2,0,3,5])) # TRUE
print(howsum(300,[30,14]))