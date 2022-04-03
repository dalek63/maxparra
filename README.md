## Pré-requis

### Partie console
Afin de pouvoir exécuter cette librairie sur votre poste, vous devez avoir Python 3.7 ou une version ulterieur

### Partie graphique 

Pour pouvoir afficher le graphes dy systeme de taches parralélisé au maximum, vous devez : 
    1. Telecharger get-pip.py file pour ensuite installer Pip qui va servir à installer les modules dans 2.( https://pip.pypa.io/en/stable/installation/)
    2. Telecharger et installez les modules networkxet matplotlib ( Networkx : https://networkx.org/documentation/stable/install.html) ( Matplotlib  : https://matplotlib.org/stable/users/installing/index.html)
 

## Note 

Le dictionnaire de tâches entré comme paramètre de TaskSystem doit posséder der clés de type int et croissantes comme par exemple : 

- list_obj = {0 : T1, 1 : T2, 2 : T3, 3 : T4, 4 : T5, 5 : T6, 6 : T7 , 7 : T8}

OU

- list_obj[len(list_obj)] = T1
- list_obj[len(list_obj)] = T2
- list_obj[len(list_obj)] = T3
- list_obj[len(list_obj)] = T4
- list_obj[len(list_obj)] = T5
- list_obj[len(list_obj)] = T6
- list_obj[len(list_obj)] = T7
- list_obj[len(list_obj)] = T8

Les fonctions qui vous seront utile sont : 
- AfficherOrdre() : Qui affiche l'ordre dans lequel les taches vont s'éxécuter suite à la   parralilasation   maximale.
- AfficherRun() : Qui execute la fonction Run de chaque tache dans l'ordre parralélisme maximale.
- afficherDependences() : Qui affiche les dependances de chaque taches.
- draw() : Qui dessine le graphe du systeme de taches parralélisées au maximum. 

Le fichier setup.py sert à installer la librairie dans nimporte quel systeme, étant donnée qu'on voulait creer une vraie librarie qu'on postera sur github, ce fichier est essentiel pour cela.

