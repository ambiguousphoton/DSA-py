def can_construct(target_word, word_bank, memory = None):
    if memory == None: memory = {}
    if target_word in memory : return memory[target_word]
    if target_word == '': return True
    for word in word_bank:
        if target_word.startswith(word):
            memory[target_word] = can_construct(target_word[len(word):], word_bank, memory)
            if memory[target_word] == True:
                return True
    memory[target_word] = False
    return False
    
print(can_construct('abcdef',['ab','abc', 'cd','def','abcd']))
print(can_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(can_construct('enterapotentpop',['a','p','ent','enter','ot','o','t']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
                    ['e',
                     'ee',
                     'eee',
                     'eeee',
                     'eeeee',
                     'eeeeeee']))