def nums(list):
    stack = []
    stack.sort()
    for  val  in list:
        if val not in stack:
            stack.append(val)
        else:
            stack.remove(val)
    return stack[0] 

print(nums([2,2,1]))