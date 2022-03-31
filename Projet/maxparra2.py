import networkx as nx
import matplotlib.pyplot as plt


    
class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None


class TaskSystem:
    def __init__(self, list_obj):
        self.list_obj = list_obj


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




    # Cette fonction permet de supprimer les redondances des taches du dictionnaire

    def redondances(self, dico):
        for i in range (len(dico)):
            for j in range(len(dico.get(i))):
                for k in range(i+1,len(dico)):
                    for l in range (len(dico.get(k))):
                        if dico.get(i).get(j)==dico.get(k).get(l) and (self.list_obj.get(k)) in dico.get(i).values():
                            dico.get(i).pop(self.getKey(dico.get(i),dico.get(k).get(l)))
        return dico

    def maxparra(self):
        return self.redondances(self.compatibleUltime(self.list_obj))

    #afficheprecedences(maxparra)   

        # Cette fonction renvoie True si la tache mis en parametres une tache n'est jamais une précedence et false sinon
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

        # Cette fonction donne l'ordre dans lequel les taches doivent s'éxecuter
    def initrun(self, dico):
        ordre = {}

        # Ici on cherche les taches qui n'ont pas de précedences et qui s'effectuent donc en premier 
        for i in range(len(dico)):
            if self.recherche(self.list_obj.get(i), dico)==False:
                self.addElement(ordre, self.list_obj.get(i))
                
        tempdic = ordre
        tempdic2 = {}
        
        # Tant qu'au moins 1 tache qu'on étudie possède au moins 1 précedence
        while self.aucunePrecedence(tempdic)==False:
            for k in range(len(tempdic)):
                for i in range (len(dico)):
                    for j in range (len(dico.get(i))):
                        if self.list_obj.get(i)==tempdic.get(k)and dico.get(i).get(j) not in tempdic2.values():
                            self.addElement(tempdic2, dico.get(i).get(j))
            
            for l in range(len(tempdic2)):
                self.addElement(ordre, tempdic2.get(l))

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
    def afficheordre(self, dico):
        if self.samename()==True:
            exit()
        for i in range(len(dico)):
            print(dico.get(i).name)

        # Cette fonction permet d'executer le run de chaque tache en respectant l'ordre trouvé juste avant
    def afficheRun(self): 
        if self.samename()==True:
            exit()
        print("")
        print("Voici l'execution des tâches dans l'ordre de paralélisation maximale : ")
        for i in range (len(self.initrun(self.maxparra()))):
            self.initrun(self.maxparra()).get(i).run=print("la tache "+ self.initrun(self.maxparra()).get(i).name + " a été lancée ")

    
        # afficherDependences sert à afficher les dependences de chaque tache du dictionnaire
    def afficheDependances(self):
        if self.samename()==True:
            exit()
        print("")
        print("Voici les dépendances de chaque tache : ")
        for i in range (len(self.list_obj)):
            print("___________________________")
            print(self.list_obj.get(i).name, " : " )
            if len(self.maxparra().get(i))==0:
                print("Aucune dépendance")
            for j in range (len(self.maxparra().get(i))):
                    print(self.maxparra().get(i).get(j).name)


    #***************************************************Partie Graphique***********************************************************


    #Fonction qui dessine le graphe par rapport à la liste des dépendances creer par la fonction redondances(compatibleUltime(list_obj)) 
    # et grâce à deux modules importés : networkx et matplotlib

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


# Des exemples qui nous ont permis de tester plus rapidement le programme

#Exemple 1

T1 = Task(name = "T1",writes = [3],reads = [1,2],run = None)
T2 = Task(name = "T2",writes = [4],reads = [1],run = None)
T3  = Task(name = "T3",writes = [1],reads = [3,4],run = None)
T4 = Task(name = "T3",writes = [5],reads = [3,4],run = None)
T5 = Task(name = "T5",writes = [2],reads = [4],run = None)
T6 = Task(name = "T6",writes = [5],reads = [5],run = None)
T7 = Task(name = "T7",writes = [4],reads = [4,1,2],run = None)
T8 = Task(name = "T8",writes = [5],reads = [1,3],run =None)

#Exemple 2 (commenter l'exemple 1 si l'on decommente l'exemple 2 et inversement )



T10 = Task(name = "T1",writes = [7],reads = [1,2],run = None)
T20= Task(name = "T2",writes = [8],reads = [3,4],run = None)
T30  = Task(name = "T3",writes = [9],reads = [5,6],run = None)
T40 = Task(name = "T4",writes = [10],reads = [7,8],run = None)
T50 = Task(name = "T5",writes = [11],reads = [7,8],run = None)
T60 = Task(name = "T6",writes = [12],reads = [9,11],run = None)
T70 = Task(name = "T7",writes = [13],reads = [12],run = None)
T80 = Task(name = "T8",writes = [14],reads = [10,13],run =None)


#list_obj est le dictionnaire qui contient toutes les tâches 

list_obj = {}

list_nul = {}
# Permet de rajouter une tache après l'autre au fur et à mesur
list_obj[len(list_obj)] = T1
list_obj[len(list_obj)] = T2
list_obj[len(list_obj)] = T3
list_obj[len(list_obj)] = T4
list_obj[len(list_obj)] = T5
list_obj[len(list_obj)] = T6
list_obj[len(list_obj)] = T7
list_obj[len(list_obj)] = T8

list_nul[len(list_nul)] = T10
list_nul[len(list_nul)] = T20
list_nul[len(list_nul)] = T30
list_nul[len(list_nul)] = T40
list_nul[len(list_nul)] = T50
list_nul[len(list_nul)] = T60
list_nul[len(list_nul)] = T70
list_nul[len(list_nul)] = T80


s1= TaskSystem(list_obj)
s1.afficheDependances()
s1.afficherRun()
s1.draw()
