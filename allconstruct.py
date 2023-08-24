memory = {}
def all_construct(target, word_bank, memory = None):
    if memory == None: memory = {}
    if target in memory: memory[target]  
    if target == '': return [[]]
    all_paths = []
    for word in word_bank:
        if target.startswith(word):
            paths = all_construct(target[len(word):], word_bank, memory )
            for path in paths:
                path.append(word)
            all_paths = paths + all_paths
    memory[target] = all_paths
    return all_paths

print(all_construct('purple',['purp','p','ur','le','purpl']), memory)
print(memory)
memory = {}
print(all_construct('abc',['ab','abc','cd','def','abcd','ef','c'], memory))
print(memory)
print(all_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz',['a','aa','aaaaaa','aaaaaaa','aaaaaaaaaaaaaa']))