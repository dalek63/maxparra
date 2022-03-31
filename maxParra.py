import networkx as nx
import matplotlib.pyplot as plt

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

def verifname(nom):                                     #Verifie si une tâche a déjà ce nom
    for i in range(len(list_obj)):
        if list_obj.get(i).name==nom:
            print("Ce nom de tâche est déjà utilisé, choisissez en un autre")
            return False


#list_obj est le dictionnaire qui contient toutes les tâches 

list_obj = {}

def ajouter():                                       # Permet de creer une tache et de l'ajouter au dictionnaire des tâches 
    
    print('Entrez nom')
    nom=input()
    while verifname(nom)==False:
        nom=input()
    name=nom
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

    self = Task(name, writes, reads, None)

    self.run=print("La tâche " + name + " a été lancée")

    addElement(list_obj, self)
    
#ajouter()
#list_obj.get(0).run

def ajouterTaches():                            # Permet d'ajouter le nombre voulu de taches
    print("Entrez le nombre de tâches")
    n=input()
    for i in range (n):
        ajouter()

    

# Des exemples qui nous ont permis de tester plus rapidement le programme

#Exemple 1

T1 = Task(name = "T1",writes = [3],reads = [1,2],run = None)
T2 = Task(name = "T2",writes = [4],reads = [1],run = None)
T3  = Task(name = "T3",writes = [1],reads = [3,4],run = None)
T4 = Task(name = "T4",writes = [5],reads = [3,4],run = None)
T5 = Task(name = "T5",writes = [2],reads = [4],run = None)
T6 = Task(name = "T6",writes = [5],reads = [5],run = None)
T7 = Task(name = "T7",writes = [4],reads = [4,1,2],run = None)
T8 = Task(name = "T8",writes = [5],reads = [1,3],run =None)

#Exemple 2 (commenter l'exemple 1 si l'on decommente l'exemple 2 et inversement )


'''
T1 = Task(name = "T1",writes = [7],reads = [1,2],run = None)
T2 = Task(name = "T2",writes = [8],reads = [3,4],run = None)
T3  = Task(name = "T3",writes = [9],reads = [5,6],run = None)
T4 = Task(name = "T4",writes = [10],reads = [7,8],run = None)
T5 = Task(name = "T5",writes = [11],reads = [7,8],run = None)
T6 = Task(name = "T6",writes = [12],reads = [9,11],run = None)
T7 = Task(name = "T7",writes = [13],reads = [12],run = None)
T8 = Task(name = "T8",writes = [14],reads = [10,13],run =None)
'''


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


# Cette fonction permet de supprimer les redondances des taches du dictionnaire

def redondances(dico):
    for i in range (len(dico)):
        for j in range(len(dico.get(i))):
            for k in range(i+1,len(dico)):
                for l in range (len(dico.get(k))):
                    if dico.get(i).get(j)==dico.get(k).get(l) and (list_obj.get(k)) in dico.get(i).values():
                        dico.get(i).pop(getKey(dico.get(i),dico.get(k).get(l)))
    return dico



maxparra = redondances(compatibleUltime(list_obj))

#afficheprecedences(maxparra)   

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

    # Ici on cherche les taches qui n'ont pas de précedences et qui s'effectuent donc en premier 
    for i in range(len(dico)):
        if recherche(list_obj.get(i), dico)==False:
            addElement(ordre, list_obj.get(i))
            
    tempdic = ordre
    tempdic2 = {}
    
    # Tant qu'au moins 1 tache qu'on étudie possède au moins 1 précedence
    while aucunePrecedence(tempdic)==False:
        for k in range(len(tempdic)):
            for i in range (len(dico)):
                for j in range (len(dico.get(i))):
                    if list_obj.get(i)==tempdic.get(k)and dico.get(i).get(j) not in tempdic2.values():
                     addElement(tempdic2, dico.get(i).get(j))
           
        for l in range(len(tempdic2)):
            addElement(ordre, tempdic2.get(l))

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
        print(dico.get(i).name)

    # Cette fonction permet d'executer le run de chaque tache en respectant l'ordre trouvé juste avant
def afficherRun(dico): 
    for i in range (len(dico)):
        dico.get(i).run=print("la tache "+ dico.get(i).name + " a été lancée ")


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





#afficheDependances(maxparra)
'''
print("")
print("Lancement des tâches en paralélisation maximale: ")
print("")
afficherRun(initrun(maxparra))


'''


#afficheordre(initrun(maxparra))

#print(aucunePrecedence(t))

afficherRun(initrun(maxparra))

draw()