not_allowed = {' ','',','}
Registers = {'register1':None,
             'register2':None,
             'register3':None,
             'register4':None,
             'register5':None,
             'register6':None,
             'register7':None,}

def extract(string):
    tokens = []
    token = '' 
    for index, char in enumerate(string):
        if char != ' ':
            token += char
        if (char == ' ' or index == len(string) - 1) and token not in not_allowed:
            tokens.append(token)
            token = ''
    # "loop 40 times"
    return tokens

def alingn_commands(string):
    commands = []
    command = ''
    for char in string:
        if char != '.':
            command += char
        else:
            commands.append(command)
            command = ''
    return commands

def tokenisatioin():
    pass

def add(numbers):
    sum_ = 0
    for number in numbers:
        sum_ += int(number)
    return sum_

def subtract(numbers):
    sum_ = 0
    for number in numbers:
        sum_ -= int(number)
    return sum_

def multiply(numbers):
    product = 1
    for number in numbers:
        product *= int(number)
    return product

def interperet(command): # ['multiply','5','4','4','3']
    tasks = {'add':add,'subtract':subtract,'multiply':multiply}
    t = tasks[command[1]]
    accumulator = t(command[1::])
    print(accumulator) 
interperet(['register1','add','34','23'])

string = 'register1 add 43 24 42 32.'

# print(alingn_commands(string))