
dictionnaireTache = { 

    "T1"    :   [],
    "T2"    :   ["T1"],
    "T3"    :   ["T1","T2"],
    "T4"    :   ["T1","T2","T3"],
    "T5"    :   ["T1", "T2", "T3","T4"],
    "T6"    :   ["T1","T2","T3","T4","T5"],
    "T7"    :   ["T1","T2","T3","T4","T5","T6"]

}


class TaskSystem: 
    def __init__(self, dictionnairePrecedence):
        self.dictionnairePrecedence = dictionnairePrecedence

    def getDependencies(nomTache):
        for val in dictionnairePrecedence.keys():
            if val == nomTache:
                print(val)
s1 = TaskSystem(dictionnaireTache)
print(s1.dictionnairePrecedence.values())
print(s1.getDependencies("T2"))
