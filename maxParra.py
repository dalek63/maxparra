
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


prout = Task(name = "setha",writes = [1],reads = [3,2],run = None)
caca = Task(name = "sakir",writes = [2],reads = [3,7],run = None)
list_obj[len(list_obj)] = prout
list_obj[len(list_obj)] = caca


def afficher(dico): 
    for i in range (len(list_obj)):
        for j in range (len(list_obj.get(i).writes)):
            print(list_obj.get(i).writes[j])
        for j in range (len(list_obj.get(i).reads)):
            print(list_obj.get(i).reads[j])


def compatible(t1,t2):
    for i in range (len(t1.writes)):
        for j in range (len(t2.reads)):
            if t1.writes[i]==t2.reads[j]:
               return False
        for j in range (len(t2.writes)):
            if t1.writes[i]==t2.writes[j]:
               return False
    for i in range (len(t2.writes)):
        for j in range (len(t1.reads)):
            if t2.writes[i]==t1.reads[j]:
               return False
    return True

def compatibletotal(t,dico):
    incompatibles = {}
    for i in range(len(dico)):
        if compatible(t, dico.get(i))==false:
                addElement(incompatibles,dico.get(i))
    return incompatibles


def compatibleUltime(dico):
    incompatibles = {}
    for i in range (len(dico)):
        for j in range (len(dico)):
            addElement(incompatibles, compatibletotal(dico.get(i),dico.get(j)))
            


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
