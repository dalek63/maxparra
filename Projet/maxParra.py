import networkx as nx
import matplotlib.pyplot as plt
from re import X
import time
import threading



class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None


def addElement(dictionnaire, element):                  # Ajouter un element à la fin du dico
    dictionnaire[len(dictionnaire)] = element

def getKey(dico,val):                                   # Retourne la clé de la valeur passé en parametre
    for i in range(len(dico)):
        if dico.get(i)==val:
            return i

def verifname(nom, liste):                                     #Verifie si une tâche a déjà ce nom
    for i in range(len(liste)):
        if liste.get(i).name==nom:
            print("Ce nom de tâche est déjà utilisé, choisissez en un autre")
            return False


#list_obj est le dictionnaire qui contient toutes les tâches 

list_obj = {}

def runT1():
    global g,a,b
    a=2
    b=1
    g=a+b
   
    
def runT2():
    global h,c,d
    c=2
    d=1
    h=c-d
   

def runT3():
    global i,e,f
    e=1
    f=1
    i=e*f
    
    
def runT4():
    global j,g,h
    j=g*h
   

def runT5():
    global k,g,h
    k=g/h
   


def runT6():
    global l,k,i
    l=k+i
   


def runT7():
    global m,l
    m=2*l
    


def runT8():
    global n,j,m
    n=j+m
    print(n)
    




T1 = Task(name = "T1",writes = [7],reads = [1,2],run = runT1())
T2= Task(name = "T2",writes = [8],reads = [3,4],run = runT2())
T3  = Task(name = "T3",writes = [9],reads = [5,6],run = runT3())
T4 = Task(name = "T4",writes = [10],reads = [7,8],run = runT4())
T5 = Task(name = "T5",writes = [11],reads = [7,8],run = runT5())
T6 = Task(name = "T6",writes = [12],reads = [9,11],run = runT6())
T7 = Task(name = "T7",writes = [13],reads = [12],run = runT7())
T8 = Task(name = "T8",writes = [14],reads = [10,13],run =runT8())



# Permet de rajouter une tache après l'autre au fur et à mesur
list_obj[len(list_obj)] = T1
list_obj[len(list_obj)] = T2
list_obj[len(list_obj)] = T3
list_obj[len(list_obj)] = T4
list_obj[len(list_obj)] = T5
list_obj[len(list_obj)] = T6
list_obj[len(list_obj)] = T7
list_obj[len(list_obj)] = T8



# Les 2 fonctions suivantes nous ont servi à tester l'affichage des Ecriture/Lecteurs de notre dictionnaire
def afficher(dico): 
    for i in range (len(dico)):
        for j in range (len(dico.get(i).writes)):
            print(dico.get(i).writes[j])
        for j in range (len(dico.get(i).reads)):
            print(dico.get(i).reads[j])



# Cette methode permet de verifier les conditions de Bernstein, elle retourne faux si une condition est violée et vrai sinon
def compatible(t1,t2):
    for i in range (len(t1.writes)):
                for j in range (len(t2.reads)):
                    if t1.writes[i]==t2.reads[j]   :
                        return False
    for i in range (len(t2.writes)):
        for j in range (len(t1.reads)):
            if t2.writes[i]==t1.reads[j]:
               return False
        for j in range (len(t2.writes)):
            if t1.writes[i]==t2.writes[j]:
               return False
    return True
   

#compatibleTotal sert à appliquer compatible entre 1 tache et tout le reste des taches
def compatibletotal(t,dico):
    incompatibles = {}                                          
    for i in range(getKey(dico,t),len(dico)):
                if compatible(t, dico.get(i))==False and dico.get(i)!=t :
                        addElement(incompatibles,dico.get(i))
    return incompatibles


# compatibleUltime sert à appliquer compatibleTotal entre toutes les taches
def compatibleUltime(dico):
    incompatibles = {}
    for i in range (len(dico)):
        addElement(incompatibles, compatibletotal(dico.get(i),dico))
    return incompatibles    


  

# Cette fonction permet de supprimer les redondances des taches du dictionnaire


def arretes(dico):
    arretes = {}
    for i in range(len(dico)):
        for j in range(len(dico.get(i))):
            addElement(arretes, [list_obj.get(i),dico.get(i).get(j)])
    return arretes        

def afficheArretes(dico):
    for i in range(len(dico)):
        print(dico.get(i)[0].name,",",dico.get(i)[1].name)

#afficheArretes(arretes(compatibleUltime(list_obj)))

# Cette fonction permet de supprimer les redondances des taches du dictionnaire

def contient(liste1,liste2):
    for idx in range(len(liste1) - len(liste2) + 1): 
            if liste1[idx : idx + len(liste2)] == liste2: 
                return True 
    return False


def newChemin(chemin, val):
    newChemin = []
    for i in range(len(chemin)):
        newChemin.append(chemin[i])
        if chemin[i]==val:
            return newChemin


def chemins():
    chemins = arretes(compatibleUltime(list_obj))
    copieArretes = arretes(compatibleUltime(list_obj)) 
    for i in range(len(chemins)):
        for j in range(len(copieArretes)):
            if chemins.get(i)[len(chemins.get(i))-1]==copieArretes.get(j)[0]:
                chemins.get(i).append(copieArretes.get(j)[1])
            if copieArretes.get(j)[0] in chemins.get(i) and chemins.get(i)[chemins.get(i).index(copieArretes.get(j)[0])+1]!=copieArretes.get(j)[1] and newChemin(chemins.get(i), copieArretes.get(j)[0])+[copieArretes.get(j)[1]] not in chemins.values():
                addElement(chemins, newChemin(chemins.get(i), copieArretes.get(j)[0])+[copieArretes.get(j)[1]])
    '''
    for k in range(len(chemins)):
        for l in range(k+1,len(chemins)):
            if contient(chemins.get(l), chemins.get(k))==True:
                chemins.pop(chemins.get(k))
                k=k+1
    '''
    return chemins

    

def afficheChemins():
    for i in range(len(chemins())):
        print("***********************")
        for j in range(len(chemins().get(i))):
            print(chemins().get(i)[j].name)




def redondances(dico):
    for i in range(len(chemins())):
        for j in range(i+1,len(chemins())):
            if chemins().get(i)[0]==chemins().get(j)[0] and chemins().get(i)[len(chemins().get(i))-1]==chemins().get(j)[len(chemins().get(j))-1]:
                
                if len(chemins().get(i))!=len(chemins().get(j)) and chemins().get(i)[len(chemins().get(i))-1] in dico.get(getKey(list_obj,chemins().get(i)[0])).values():
                   
                    dico.get(getKey(list_obj,chemins().get(i)[0] )).pop(getKey(dico.get(getKey(list_obj,chemins().get(i)[0] )),chemins().get(i)[len(chemins().get(i))-1]))
               
    return dico

maxparra = redondances(compatibleUltime(list_obj))

  

  # afficherprecedeces sert à afficher les precedences de chaque tache du dictionnaire
def afficheDependances(dico):
    print("Voici les dépendances de chaque tache : ")
    print("")
    for i in range (len(list_obj)):
        print(list_obj.get(i).name, " : " )
        if len(dico.get(i))==0:
            print("Aucune dépendance")
        for j in range (len(dico.get(i))):
                print(dico.get(i).get(j).name)

    # Cette fonction renvoie True si la tache mis en parametres une tache n'est jamais une précedence et false sinon
def recherche(t,dico):
    for i in range(len(dico)):
        for j in range(len(dico)):
                if t in dico.get(j).values():
                    return True
    return False

    # Cette fonction applique la fonction recherche dans le dictionnaire de tache
def aucunePrecedence(dico):
    for i in range (len(dico)):
        for j in range(len(list_obj)):
            if dico.get(i)==list_obj.get(j) and len(maxparra.get(j))!=0: 
                return False
    return True

    # Cette fonction donne l'ordre dans lequel les taches doivent s'éxecuter
def initrun(dico):
    ordre = {}
    tempdic = {}
    # Ici on cherche les taches qui n'ont pas de précedences et qui s'effectuent donc en premier 
    for i in range(len(dico)):
        if recherche(list_obj.get(i), dico)==False:
            addElement(tempdic, list_obj.get(i))
    addElement(ordre, tempdic)   
    tempdic2 = {}
    
    # Tant qu'au moins 1 tache qu'on étudie possède au moins 1 précedence
    while aucunePrecedence(tempdic)==False:
        for k in range(len(tempdic)):
            for i in range (len(dico)):
                for j in range (len(dico.get(i))):
                    if list_obj.get(i)==tempdic.get(k) and dico.get(i).get(j) not in tempdic2.values():
                        addElement(tempdic2, dico.get(i).get(j))
           
        
        addElement(ordre, tempdic2)

        tempdic=tempdic2
         
        '''
        print(aucunePrecedence(tempdic))
        print("!")
        for l in range(len(tempdic)):
            print(tempdic.get(l).name)
        print("!")
        '''
        tempdic2 = {}

       
    return ordre       

    # Cette fonction permet d'afficher l'ordre des taches
def afficheordre(dico):
    for i in range(len(dico)):
        print("**************************")
        for j in range(len(dico.get(i))):
            print(dico.get(i).get(j).name)

    # Cette fonction permet d'executer le run de chaque tache en respectant l'ordre trouvé juste avant





def lancement(dico):
    k=0
    for i in range(len(dico)):
        for j in range(len(dico.get(i))):
            globals()['t'+str(k)]=threading.Thread(target=dico.get(i).get(j).run)

    for l in range(k):
        for i in range(len(dico)):
            for j in range(len(dico.get(i))):
                globals()['t'+str(l)].start()
                print("")
            for j in range(len(dico.get(i))):
                globals()['t'+str(l)].join()
            



#***************************************************Partie Graphique***********************************************************


#Fonction qui dessine le graphe par rapport à la liste des dépendances creer par la fonction redondances(compatibleUltime(list_obj)) 
# et grâce à deux modules importés : networkx et matplotlib

def draw():
    G = nx.DiGraph()
    arretes = []
    for i in range(len(maxparra)):
        for j in range(len(maxparra.get(i))):
            arretes.append((list_obj.get(i).name, maxparra.get(i).get(j).name))

    G.add_edges_from(arretes)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G, pos)
    plt.show()

'''

# Des exemples qui nous ont permis de tester plus rapidement le programme

#Exemple 1

'''





lancement(initrun(maxparra))

#afficheordre(initrun(maxparra))

#draw()