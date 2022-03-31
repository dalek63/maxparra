## Pré-requis

### Partie console
Afin de pouvoir exécuter cette librairie sur votre poste, vous devez avoir Python 3.7 ou une version ulterieur

### Partie graphique 

Pour pouvoir afficher le graphes dy systeme de taches parralélisé au maximum, vous devez : 
    1. Telecharger get-pip.py file pour ensuite installer Pip qui va servir à installer les modules dans 2.( https://pip.pypa.io/en/stable/installation/)
    2. Telecharger et installez les modules networkxet matplotlib ( Networkx : https://networkx.org/documentation/stable/install.html) ( Matplotlib  : https://matplotlib.org/stable/users/installing/index.html)
 

## Note 
Les fonctions qui vous seront utile sont : 
- AfficherOrdre() : Qui affiche l'ordre dans lequel les taches vont s'éxécuter suite à la   parralilasation   maximale.
- AfficherRun() : Qui execute la fonction Run de chaque tache dans l'ordre parralélisme maximale.
- afficherDependences() : Qui affiche les dependances de chaque taches.
- draw() : Qui dessine le graphe du systeme de taches parralélisées au maximum. 

Le fichier setup.py sert à installer la librairie dans nimporte quel systeme, étant donnée qu'on voulait creer une vraie librarie qu'on postera sur github, ce fichier est essentiel pour cela.