import networkx as nx
import matplotlib.pyplot as plt
from re import X
import time
import threading

#Création de la classe Task    
class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None

#Création de la classe Task System ( le système de tache )
class TaskSystem:
    def __init__(self, list_obj):
        self.list_obj = list_obj


    #BONUS 1 : Fonction samename qui est lancé dans chaque fonction utile de TaskSystem pour savoir si deux tâches ont un même nom
    def samename(self):
        for i in range(len(self.list_obj)):
            for j in range(i+1,len(self.list_obj)):
                if self.list_obj.get(i).name == self.list_obj.get(j).name :
                    print("DEUX TACHES ONT LE MEME NOM , FIN DU PROGRAMME")
                    return True
        return False
      
    def addElement(self, dictionnaire, element):                  # Ajouter un element à la fin du dico
        dictionnaire[len(dictionnaire)] = element

    def getKey(self, dico,val):                                   # Retourne la clé de la valeur passé en parametre
        for i in range(len(dico)):
            if dico.get(i)==val:
                return i

    # Cette methode permet de verifier les conditions de Bernstein, elle retourne faux si une condition est violée et vrai sinon
    def compatible(self, t1,t2):
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
    

    #compatibleTotal sert à appliquer compatible entre 1 tache et tout le reste des taches
    def compatibletotal(self,t,dico):
        incompatibles = {}                                          
        for i in range(self.getKey(dico,t),len(dico)):
                    if self.compatible(t, dico.get(i))==False and dico.get(i)!=t :
                            self.addElement(incompatibles,dico.get(i))
        return incompatibles


    # compatibleUltime sert à appliquer compatibleTotal entre toutes les taches
    def compatibleUltime(self, dico):
        incompatibles = {}
        for i in range (len(dico)):
            self.addElement(incompatibles,self.compatibletotal(dico.get(i),dico))
        return incompatibles    


    #Fonction retournant un dicionnaires de toutes les liaisons (ou arretes) du graphe

    def arretes(self,dico):
        arretes = {}
        for i in range(len(dico)):
            for j in range(len(dico.get(i))):
                self.addElement(arretes, [self.list_obj.get(i),dico.get(i).get(j)])
        return arretes        

    #Fonction créent un nouveau chemin ( nécessaire pour la fonction chemins() )

    def newChemin(self, chemin, val):
        newChemin = []
        for i in range(len(chemin)):
            newChemin.append(chemin[i])
            if chemin[i]==val:
                return newChemin

    #Fonction réalisant un dictionnaire de tout les chemins existant sous forme de tableaux

    def chemins(self):
        chemins = self.arretes(self.compatibleUltime(self.list_obj))
        copieArretes = self.arretes(self.compatibleUltime(self.list_obj)) 
        for i in range(len(chemins)):
            for j in range(len(copieArretes)):
                if chemins.get(i)[len(chemins.get(i))-1]==copieArretes.get(j)[0]:
                    chemins.get(i).append(copieArretes.get(j)[1])
                if copieArretes.get(j)[0] in chemins.get(i) and chemins.get(i)[chemins.get(i).index(copieArretes.get(j)[0])+1]!=copieArretes.get(j)[1] and self.newChemin(chemins.get(i), copieArretes.get(j)[0])+[copieArretes.get(j)[1]] not in chemins.values():
                    self.addElement(chemins, self.newChemin(chemins.get(i), copieArretes.get(j)[0])+[copieArretes.get(j)[1]])
        
        return chemins

    #Fonction retirant les dépendances créant une redondance pour une tâche 

    def redondances(self, dico):
        for i in range(len(self.chemins())):
            for j in range(i+1,len(self.chemins())):
                if self.chemins().get(i)[0]==self.chemins().get(j)[0] and self.chemins().get(i)[len(self.chemins().get(i))-1]==self.chemins().get(j)[len(self.chemins().get(j))-1]:
                    
                    if len(self.chemins().get(i))!=len(self.chemins().get(j)) and self.chemins().get(i)[len(self.chemins().get(i))-1] in dico.get(self.getKey(self.list_obj,self.chemins().get(i)[0])).values():
                    
                        dico.get(self.getKey(self.list_obj,self.chemins().get(i)[0] )).pop(self.getKey(dico.get(self.getKey(self.list_obj,self.chemins().get(i)[0] )),self.chemins().get(i)[len(self.chemins().get(i))-1]))
                
        return dico


    #Fonction de simplification 
    def maxparra(self):
        return self.redondances(self.compatibleUltime(self.list_obj))

     

    # Cette fonction renvoie True si la tache mis en parametres une tache n'est jamais une dépendance et false sinon

    def recherche(self, t,dico):
        for i in range(len(dico)):
            for j in range(len(dico)):
                    if t in dico.get(j).values():
                        return True
        return False

    # Cette fonction applique la fonction recherche dans le dictionnaire de tache

    def aucunePrecedence(self, dico):
        for i in range (len(dico)):
            for j in range(len(self.list_obj)):
                if dico.get(i)==self.list_obj.get(j) and len(self.maxparra().get(j))!=0: 
                    return False
        return True

    # Cette fonction donne l'ordre dans lequel les taches doivent s'éxecuter et celles qui doivent s'executer en parallele

    def initrun(self, dico):
        ordre = {}
        tempdic = {}

        # Ici on cherche les taches qui n'ont pas de dépendances et qui s'effectuent donc en premier 
        for i in range(len(dico)):
            if self.recherche(self.list_obj.get(i), dico)==False:
                self.addElement(tempdic, self.list_obj.get(i))
                
        self.addElement(ordre, tempdic)
        tempdic2 = {}
        
        # Tant qu'au moins 1 tache qu'on étudie possède au moins 1 Dépendance
        while self.aucunePrecedence(tempdic)==False:
            for k in range(len(tempdic)):
                for i in range (len(dico)):
                    for j in range (len(dico.get(i))):
                        if self.list_obj.get(i)==tempdic.get(k)and dico.get(i).get(j) not in tempdic2.values():
                            self.addElement(tempdic2, dico.get(i).get(j))
            
            
            self.addElement(ordre, tempdic2)
 
            tempdic=tempdic2
            tempdic2 = {}

        
        return ordre       

    # Cette fonction permet d'afficher les tâches dans leur ordre d'execution en paralélisme maximal et montre les tâches qui sont parallèles entre elles

    def afficheordre(self):
        for i in range(len(self.initrun(self.maxparra()))):
            print("**************************")
            for j in range(len(self.initrun(self.maxparra()).get(i))):
                print(self.initrun(self.maxparra()).get(i).get(j).name)
        

    #Cette fonction sert à éxécuter chaque thread de tâche de manière à ce qu'elles soient exécuter dans l'ordre de paralélisme maximale 

    def execution(self):
        k=0
        for i in range(len(self.initrun(self.maxparra()))):
            for j in range(len(self.initrun(self.maxparra()).get(i))):
                globals()['t'+str(k)]=threading.Thread(target=self.initrun(self.maxparra()).get(i).get(j).run)

        for l in range(k):
            for i in range(len(self.initrun(self.maxparra()))):
                for j in range(len(self.initrun(self.maxparra()).get(i))):
                    globals()['t'+str(l)].start()
                    print("")
                for j in range(len(self.initrun(self.maxparra()).get(i))):
                    globals()['t'+str(l)].join()
        
    # afficherDependences sert à afficher les dependences de chaque tache du dictionnaire

    def afficheDependances(self):
        if self.samename()==True:
            exit()
        print("")
        print("Voici les dépendances de chaque tache : ")
        for i in range (len(self.list_obj)):
            print("******************************")
            print(self.list_obj.get(i).name, " : " )
            if len(self.maxparra().get(i))==0:
                print("Aucune dépendance")
            for j in range (len(self.maxparra().get(i))):
                    print(self.maxparra().get(i).get(j).name)


    #***************************************************Partie Graphique***********************************************************


    #Fonction qui dessine le graphe par rapport à la liste des dépendances creer par la fonction redondances(compatibleUltime(list_obj)) 
    # et grâce à deux modules importés : networkx et matplotlib
    #BONUS 2 

    def draw(self):
        if self.samename()==True:
            exit()
        G = nx.DiGraph()
        arretes = []
        for i in range(len(self.maxparra())):
            for j in range(len(self.maxparra().get(i))):
                arretes.append((self.list_obj.get(i).name, self.maxparra().get(i).get(j).name))

        G.add_edges_from(arretes)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)
        plt.show()


#*************************************************Execution du code*****************************************************************
#Exemple 


#Fonctions de chaque tâche 

def runT1():
    global m1,m2,m3
    m1=1
    m2=1
    m3=m1+m2
   
    
def runT2():
    global m1,m4
    m4=m1*3
    

def runT3():
    global m1,m3,m4
    m1 = m3+m4
   
    
def runT4():
    global m3,m4,m5
    m5=m3+m4
   

def runT5():
    global m4,m2
    m2=2*m4
  


def runT6():
    global m5
    m5=2*m5
  
    

def runT7():
    global m1,m2,m4
    m4 = m1*m2
   


def runT8():
    global m5,m1,m2
    m5=m1+m3
    print(m5)
    
# Des exemples qui nous ont permis de tester plus rapidement le programme

#Exemple 1

T1 = Task(name = "T1",writes = [3],reads = [1,2],run = runT1())
T2 = Task(name = "T2",writes = [4],reads = [1],run = runT2())
T3  = Task(name = "T3",writes = [1],reads = [3,4],run = runT3())
T4 = Task(name = "T4",writes = [5],reads = [3,4],run = runT4())
T5 = Task(name = "T5",writes = [2],reads = [4],run = runT5())
T6 = Task(name = "T6",writes = [5],reads = [5],run = runT6())
T7 = Task(name = "T7",writes = [4],reads = [4,1,2],run = runT7())
T8 = Task(name = "T8",writes = [5],reads = [1,3],run =runT8())

#list_obj est le dictionnaire qui contient toutes les tâches, il faut que le dictionnaire aient des clés 

list_obj = {}


list_obj = {0 : T1, 1 : T2, 2 : T3, 3 : T4, 4 : T5, 5 : T6, 6 : T7 , 7 : T8}



s1= TaskSystem(list_obj)
s1.afficheDependances()
s1.afficheordre()
s1.execution()
s1.draw()
