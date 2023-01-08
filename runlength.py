#  aaabbcccd

def runlength_encoding(string):
    previous = None
    character = ""
    counter = 1
    new_string = ""
    for i in string:
        character = i
        if previous == character :
            counter +=1 
        elif previous != None:
            new_string += f"{counter}{previous}" 
            counter = 1
        previous = character
    return new_string

a = input("enter the string : ")
print(runlength_encoding(a+"!"))

def runlength_decoding(string):
    number = 0
    decoded_string = ""
    string_counter = 0  
    for i in string:
        if string_counter % 2 != 0:
            for j in range(number):
                decoded_string += i 
        else:
            number = int(i)
        string_counter += 1

    return decoded_string        

string = input("enter string to decode : ")
print(runlength_decoding(string))