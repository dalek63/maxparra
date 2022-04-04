from re import X
import time
import threading

def runT1():
    global X
    X = 2
    time.sleep(2)
   

def runT2():
    global Z
    Z = 4
    time.sleep(2)
    

def runT3():
    global X, Z
    X = X + Z
    time.sleep(2)
    

def runT4():
    global Y, X, Z
    Y = X + Z
    time.sleep(2)
    

def runT5():
    global Y
    

t1 = threading.Thread(target=runT1)
t2 = threading.Thread(target=runT2)
t3 = threading.Thread(target=runT3)
t4 = threading.Thread(target=runT4)
t5 = threading.Thread(target=runT5)

t1.start()
t2.start()

t1.join()
t2.join()

t3.start()
t3.join()

t4.start()

