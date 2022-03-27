from tkinter import *

class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None


def addElement(dictionnaire, element):
    dictionnaire[len(dictionnaire)] = element

def getKey(dico,val):
    for i in range(len(dico)):
        if dico.get(i)==val:
            return i


list_obj = {}

def ajouter(dic):
    
    print('Entrez nom')
    name=input()

    print('Entrez le nombre de valeur ecrites')
    a=input()
    n=int(a)
    writes = []
    for i in range(n):
        print('Entrez valeur ecrite')
        x=input()
        writes.append(x)
            
    print('Entrez le nombre de valeur lues')
    n=int(input())
    reads = []
    for i in range(n):
        print('Entrez valeur lue')
        x=input()
        reads.append(x)
    '''
    print('Entrez le nom de run')
    run=input()
    '''
    self = Task(name, writes, reads, None)
    addElement(list_obj, self)
    
    
#ajouter(list_obj)


T1 = Task(name = "T1",writes = [3],reads = [1,2],run = None)
T2 = Task(name = "T2",writes = [4],reads = [1],run = None)
T3  = Task(name = "T3",writes = [1],reads = [3,4],run = None)
T4 = Task(name = "T4",writes = [5],reads = [3,4],run = None)
T5 = Task(name = "T5",writes = [2],reads = [4],run = None)
T6 = Task(name = "T6",writes = [5],reads = [5],run = None)
T7 = Task(name = "T7",writes = [4],reads = [4,1,2],run = None)
T8 = Task(name = "T8",writes = [5],reads = [1,3],run = None)

list_obj[len(list_obj)] = T1
list_obj[len(list_obj)] = T2
list_obj[len(list_obj)] = T3
list_obj[len(list_obj)] = T4
list_obj[len(list_obj)] = T5
list_obj[len(list_obj)] = T6
list_obj[len(list_obj)] = T7
list_obj[len(list_obj)] = T8



def afficher(dico): 
    for i in range (len(dico)):
        for j in range (len(dico.get(i).writes)):
            print(dico.get(i).writes[j])
        for j in range (len(dico.get(i).reads)):
            print(dico.get(i).reads[j])

def afficherNoms(dico): 
    for i in range (len(dico)):
        print(i , " : ")
        for j in range (len(dico.get(i))):
            print(dico.get(i).get(j).name)

'''
def compatible(t1,t2):
    for i in range (len(t1.writes)):
        for j in range (len(t2.reads)):
            if t1.writes[i]==t2.reads[j]:
               return False
        for j in range (len(t2.writes)):
            if t1.writes[i]==t2.writes[j]:
               return False
    return True
'''

#Compatibilité inversée

def compatible(t1,t2):
    for i in range (len(t1.writes)):
        for j in range (len(t2.reads)):
            if t1.writes[i]==t2.reads[j]:
                return False
    for i in range (len(t2.writes)):
        for j in range (len(t1.reads)):
            if t2.writes[i]==t1.reads[j]:
               return False
        for j in range (len(t2.writes)):
            if t1.writes[i]==t2.writes[j]:
               return False
    return True
   

def compatibletotal(t,dico):
    incompatibles = {}                                          
    for i in range(getKey(dico,t),len(dico)):
                if compatible(t, dico.get(i))==False and dico.get(i)!=t :
                        addElement(incompatibles,dico.get(i))
    return incompatibles


def compatibleUltime(dico):
    incompatibles = {}
    for i in range (len(dico)):
        addElement(incompatibles, compatibletotal(dico.get(i),dico))
    return incompatibles    

def afficheprecedences(dico):
    print("Voici les précédences de chaque taches par leur nom")
    for i in range (len(list_obj)):
        print(list_obj.get(i).name, " : " )
        if len(dico.get(i))==0:
            print("Aucune précédence")
        for j in range (len(dico.get(i))):
                print(dico.get(i).get(j).name)

afficheprecedences(compatibleUltime(list_obj))




'''
def redondances(dico):
    for i in range(len(list_obj)):
        if(len(dico.get(i)==0)):
            i=i+1
        for j in range(len(dico.get(i))):
            while len(dico.get(i).get(j)
            for(k in range())
'''

        





#afficherNoms((compatibleUltime(list_obj)))

#print(compatible(prout,caca))              
                
#afficher(list_obj)