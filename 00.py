def om():
    list=[5,2,3,4,6,9,6,6,6,7,7,9,9,18,7,6,9,9
         ]
    list.append(99)

    tuple = (1,3,4,5,6,7)
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
    dictionary['jai_shree_ram !'] =777
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


def find_missing_number(nums):
    a = nums.copy()
    a.sort()
    for i in range(0, len(nums)+1):
        if i != a[i]:
            return i

print(find_missing_number([9, 6, 4, 2, 3, 5, 1, 0]))
