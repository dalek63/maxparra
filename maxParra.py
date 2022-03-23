
class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None


def addElement(dictionnaire, element):
    dictionnaire[len(dictionnaire)] = element

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


prout = Task(name = "prout",writes = [7],reads = [1,2],run = None)
caca = Task(name = "caca",writes = [8],reads = [3,4],run = None)
remi  = Task(name = "remi",writes = [9],reads = [5,6],run = None)
setha = Task(name = "setha",writes = [10],reads = [7,8],run = None)
gianny = Task(name = "gianny",writes = [11],reads = [7,8],run = None)
zach = Task(name = "zach",writes = [12],reads = [11,9],run = None)
younes = Task(name = "younes",writes = [13],reads = [12],run = None)
gringo = Task(name = "gringo",writes = [14],reads = [10,13],run = None)

list_obj[len(list_obj)] = prout
list_obj[len(list_obj)] = caca
list_obj[len(list_obj)] = remi
list_obj[len(list_obj)] = setha
list_obj[len(list_obj)] = gianny
list_obj[len(list_obj)] = zach
list_obj[len(list_obj)] = younes
list_obj[len(list_obj)] = gringo



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


def compatible(t1,t2):
    for i in range (len(t1.writes)):
        for j in range (len(t2.reads)):
            if t1.writes[i]==t2.reads[j]:
               return False
        for j in range (len(t2.writes)):
            if t1.writes[i]==t2.writes[j]:
               return False
    return True

def compatibletotal(t,dico):
    incompatibles = {}                                          
    for i in range(len(dico)):
        if compatible(t, dico.get(i))==False and dico.get(i)!=t:
                addElement(incompatibles,dico.get(i))
    return incompatibles


def compatibleUltime(dico):
    incompatibles = {}
    for i in range (len(dico)):
        addElement(incompatibles, compatibletotal(dico.get(i),dico))
    return incompatibles    


afficherNoms((compatibleUltime(list_obj)))

#print(compatible(prout,caca))              
                
#afficher(list_obj)

'''



        


for i, j in list_obj.items():
    print(i)
    for key in j:
        print


'''


#def ajouterV2(t):
#  list_obj.append(t)
