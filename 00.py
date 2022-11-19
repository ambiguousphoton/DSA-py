def om():
    list=[5,3,4]
    list.append(99)

    tuple = (1,2,3,4,5)
    print(type(tuple))
    return list
ls = om()
print (ls)

tuple =(2,0)
print(tuple)

def dictionary():
    dictionary = {
        "jai": 5,
        "hariom": 7,
        "bad": 00000
        }
    print ( dictionary["hariom"])
    print(dictionary)
    del dictionary["bad"]
    dictionary['jai_shree_ram'] =777
    print(dictionary)

    
dictionary()


def what_are_sets():
    s = set()
    s =set("jai shree ram")
    print (s)
    pass
what_are_sets()

stack=[]
stack.append(10)