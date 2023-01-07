def inp():
    arr = []
    while(True):
        arr.append(int(input("enter element  = ")))
        if arr[-1] == -404:
            arr.remove(-404)
            return(arr)

def bubblesort():
    arr = inp()
    sorted = 0
    for n in range(len(arr)):
        if (sorted == len(arr)):
            break
        for n in range(len(arr )- sorted):     
            if (n==(len(arr)-sorted) -1):
                break
            
            elif (arr[n]>arr[n+1]) :
                temp=arr[n+1]
                arr[n+1] = arr[n]
                arr[n] = temp
             
            print(arr)
        sorted +=1
        print(arr)
        
bubblesort()