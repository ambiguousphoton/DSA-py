import threading 
from time import sleep
Thread = threading.Thread
def hello(n,m):
    for  i in range(1,n):
        print(f'hello {i} ')
        sleep(m)

def konichiwa(n,m):
    for  i in range(1,n):
        print(f'konichiwa {i} ')
        sleep(m)

def namaste(n,m):
    for i in range (1,n):
        print(f"namaste {i} ")
        sleep(m)

if __name__ == "__main__":
    t = Thread(target= hello, args=(5,0.5))
    t2 = Thread(target=konichiwa,args=(5,1))
    t3 = Thread(target=namaste,args=(5,1))
    t.start()
    t2.start()
    t3.start() 
    print("end")
    print(f"active threading count :: {threading.active_count()}")

    sleep(5)
    print(f"active threading count :: {threading.active_count()}")