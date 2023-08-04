stack = []
a = 1
def push():
    inp = input("enter a number :")
    stack.append(inp)
    print(stack)

def pop_elm():
    if not stack:
        print("stack is already empty!")
    else:
        poped = stack.pop()
        print(stack ," - ", poped)

def loop():
    while True:
        inp = input ("enter any operation - pop , push , quit : ")
        if inp == "pop":
            pop_elm()
        elif inp == "push" :
            push()
        elif inp == "quit":
            break 
        else:
            print("wrong input !!!")

loop()
