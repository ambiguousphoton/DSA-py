def similar_char_count(string1, string2) -> bool:
    if len(string1) != len(string2):
        return False
    arr1 = [0 for i in range(128)]
    arr2 = [0 for i in range(128)] 
    for char in string1:
        arr1[ord(char)] += 1

    for char in string2:
        arr2[ord(char)] += 1
    
    for i in range(len(string1)):
        if arr1[i] != arr2[i]:
            return False
    return True
a = "dfklsjfkljajfkjakjfkljakjkldskjfk"
b = "kjakjfkljadskjfkkjkldfklsjfkljajf"
print(similar_char_count(a, b))
         
    