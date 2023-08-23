def count_construct(target, word_bank, memory = None):
    if memory == None: memory = {}
    if target in memory : return memory[target]
    if target == '' : return 1
    adder = 0
    for word in word_bank:
        if target.startswith(word):
            memory[word] = count_construct(target[len(word):], word_bank, memory)
            adder += memory[word]
    memory[target] = adder
    return adder

print(count_construct('purple',['purp','p','ur','le','purpl']))
print(count_construct('abcdef',['ab','abc', 'cd','def','abcd']))
print(count_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    ['e',
                     'ee',
                     'eee',
                     'eeee',
                     'eeeee',
                     'eeeeeee']))
