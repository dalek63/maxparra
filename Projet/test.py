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
    global m1,m2,m3
    m1=1
    m2=1
    m3=m1+m2
    return m3

def runT2():
    global m1,m4
    m4=m1*3
    

def runT3():
    global m1,m3,m4
    m1 = m3+m4
    print(m1)
   

T1 = Task(name = "T1",writes = [7],reads = [1,2],run = runT1())
T2 = Task(name = "T2",writes = [4],reads = [1],run = runT2())
T3  = Task(name = "T3",writes = [1],reads = [3,4],run = runT3())


t1=threading.Thread(target=T1.run)
t2=threading.Thread(target=T2.run)
t3=threading.Thread(target=T3.run)
t4=threading.Thread(target=T3.run)
t5=threading.Thread(target=T2.run)

t1.start()
t2.start()

t1.join()
t1.join()

t3.start()

t3.join()

t5.start()

t5.join()

t4.start()

t4.join()