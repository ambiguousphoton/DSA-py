from timeit import default_timer as timer

def linear_search(input ,list):
    for index , value in enumerate(list):
        if value == input:
            return index 

def binary_search(input,list):
    min_i = 0
    max_i = len(list) - 1
    while True:
        if min_i == max_i:
            return -1
        mid = (max_i - min_i)//2
        mid_i = min_i + mid 
        if list[mid_i] == input:
            return mid_i
        elif list[mid_i] > input:
            max_i -= mid
        elif list[mid_i] < input:
            min_i += mid
            
# [a b c d e f g h i j k]
#  0 1 2 3 4 5 6 7 8 9 10
if __name__ == "__main__":
    list = [1,33,4,54,534,3333,5,0,2,3,6,3,5,3,5,5,3,23353,5323,5,3,5,2354,453453,345,5,4,0,3434,44,534,5435,5,4,53,5,32355,353,5,777]

    start = timer()    
    l = linear_search(777,list)
    end = timer()
    t1 = start - end
    print("Linear search")
    if l == -1:
        print("element not found")
    else:
        print(f"done element found on index {l}")
    print(f"time taken by linear search = {t1}\n ....................................................................................")
    slist = sorted(list)
    print(slist)
    start = timer()
    b = binary_search(777,slist)
    end = timer()
    t2 = start - end
    print("Binary Search")
    if l == -1:
        print("element not found")
    else:
        print(f"done element found on index {b}")
    print(f"time taken by binary search = {t2}\n ....................................................................................")

    print(f"min of both is ::{min(t1,t2)}\n and ratio is ::{t1/t2}\n slower by {(1-(t1/t2)) * 100}%")
    