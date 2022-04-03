class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None

def addElement(dictionnaire, element):                  # Ajouter un element à la fin du dico
    dictionnaire[len(dictionnaire)] = element


list_obj = { }

T1 = Task(name = "T1",writes = [3],reads = [1,2],run = None)
T2 = Task(name = "T2",writes = [4],reads = [1],run = None)
T3  = Task(name = "T3",writes = [1],reads = [3,4],run = None)
T4 = Task(name = "T4",writes = [5],reads = [3,4],run = None)


list_obj[len(list_obj)] = T1
list_obj[len(list_obj)] = T2
list_obj[len(list_obj)] = T3
list_obj[len(list_obj)] = T4

dico = { }




x=[T1,T2]
y=[T3,T4]

dico[len(dico)]=x
dico[len(dico)]=y


dico1 = { }

dico1[0]={0 : T2, 1 : T3}
dico1[1]={0 : T3}
dico1[2]={0 : T4}
dico1[3]={}


def arretes(dico):
    arretes = {}
    for i in range(len(dico)):
        for j in range(len(dico.get(i))):
            arretes[len(arretes)]= [list_obj.get(i),dico.get(i).get(j)]
    return arretes

def afficheArretes(dico):
    for i in range(len(dico)):
        print(dico.get(i)[0].name,",",dico.get(i)[1].name)


def chemins():
    chemins = arretes(dico1)
    copieArretes = arretes(dico1) 
    for i in range(len(chemins)):
        for j in range(len(copieArretes)):
            if chemins.get(i)[len(chemins.get(i))-1]==copieArretes.get(j)[0]:
                chemins.get(i).append(copieArretes.get(j)[1])
    return chemins

def afficheChemins():
    for i in range(len(chemins())):
        print("***********************")
        for j in range(len(chemins().get(i))):
            print(chemins().get(i)[j].name)

#afficheChemins()


x=[T1,T2,T3,T4]
y=[T2,T3]



def contient(liste1,liste2):
    for idx in range(len(liste1) - len(liste2) + 1): 
            if liste1[idx : idx + len(liste2)] == liste2: 
                return True 
    return False
print(x[3].name)

#x.append(T3)


#afficheArretes(arretes(dico1))

