import inspect

def quick_sort(list):  
    pivot = 0
    ptr1 = 0
    ptr2 = len(list) - 1
    while True:
        if  ptr1>= ptr2:
            pivot = ptr1
            l1 = quick_sort(list[ptr1:pivot - 1])
            l2 = quick_sort(list[pivot + 1:ptr2])
            return l1 + pivot + l2 

        if  ptr1>pivot:pass
        else: ptr1+=1
        
        if not (list[ptr2] < pivot):
            ptr2 -=1

        if list[ptr1] > list[ptr2]:
            temp = list[ptr1]
            list[ptr1] = list[ptr2]
            list[ptr2] = temp
        print(ptr1," ",ptr2)

if __name__ == "__main__":
    list=[1,4,2,50,3,70,6,80,9]
    print(list)
    # print(quick_sort(list))
    print(inspect.getsource(sorted))

#[    1    ,     3      ,2,5,4,7,6,8,9]

