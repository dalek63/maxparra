
dictionnaireTache = { 

    "T1"    :   [],
    "T2"    :   ["T1"],
    "T3"    :   ["T1","T2"],
    "T4"    :   ["T1","T2","T3"],
    "T5"    :   ["T1", "T2", "T3","T4"],
    "T6"    :   ["T1","T2","T3","T4","T5"],
    "T7"    :   ["T1","T2","T3","T4","T5","T6"]

}

dictionnaireTache2 = {
    "T1" : [],
    "T2" : ["T1"],
    "Tsomme" : ["T1", "T2"]
}
"""
class Task:
    name = ""
    reads = []
    writes = []
    run = None

X = None
Y = None
Z = None
def runT1():
    global X
    X = 1

def runT2():
    global Y
    Y = 2
def runTsomme():
    global X, Y, Z
    Z = X + Y

t1 = Task()
t1.name = "T1"
t1.writes = ["X"]
t1.run = runT1
t2 = Task()
t2.name = "T2"
t2.writes = ["Y"]
t2.run = runT2
tSomme = Task()
tSomme.name = "somme"
tSomme.reads = ["X", "Y"]
tSomme.writes = ["Z"]
tSomme.run = runTsomme
"""
class TaskSystem: 
    def __init__(self, dictionnairePrecedence):
        self.dictionnairePrecedence = dictionnairePrecedence

    def getDependencies(nomTache):
        for val in dictionnairePrecedence.keys():
            if val == nomTache:
                print(val)
s1 = TaskSystem(dictionnaireTache2)
print(s1.dictionnairePrecedence.values())
