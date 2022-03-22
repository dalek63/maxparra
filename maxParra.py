
class Task:
    def __init__(self, name, writes, reads, run):
        self.name = name
        self.writes = writes
        self.reads = reads
        self.run = None

    def ajouter(self):
        list_obj = {}
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

        print('Entrez le nom de run')
        run=input()
        self = Task(name, writes, reads, run)
        list_obj.append(self)
        print(list_obj)
    
    ajouter(self)


def compatible(t1,t2):
    for key in t1.writes:
        for val in t2.reads:
            if t1.writes.key==t2.reads.val:
               return false
    return true



#def ajouterV2(t):
#  list_obj.append(t)
