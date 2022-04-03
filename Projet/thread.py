from re import X
import time
import threading


class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None


def runT1():
    global g,a,b
    a=1
    b=1
    g=a+b
    time.sleep(0.3)
    
def runT2():
    global h,c,d
    c=2
    d=1
    h=c-d
    time.sleep(0.3)

def runT3():
    global i,e,f
    e=1
    f=1
    i=e*f
    time.sleep(0.3)
    

list_obj = {}


T1 = Task(name = "T1",writes = [7],reads = [1,2],run = runT1())
T2= Task(name = "T2",writes = [8],reads = [3,4],run = runT2())
T3  = Task(name = "T3",writes = [9],reads = [5,6],run = runT3())

list_obj[len(list_obj)] = T1
list_obj[len(list_obj)] = T2
list_obj[len(list_obj)] = T3



'''
t1 = threading.Thread(target=T1.run)
t2 = threading.Thread(target=T2.run)

t1.start()
t2.start()

t1.join()
t2.join()

'''

t1=threading.Thread(target=T1.run)

t2=threading.Thread(target=T1.run)

t1.start()
t1.join()

t2.start()
t1.join()