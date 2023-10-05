import random
import matplotlib.pyplot as plt
import networkx as nx 

class Graphe:
    def __init__(self, nombre_de_noeuds):
        self.nombre_de_noeuds = nombre_de_noeuds
        self.matrice_adjacence = [[False] * nombre_de_noeuds for _ in range(nombre_de_noeuds)]
        self.couleurs = []

    def generer_couleurs(self):
        couleurs_possibles = ["rouge", "vert", "bleu"]
        self.couleurs = [random.choice(couleurs_possibles) for _ in range(self.nombre_de_noeuds)]

    def generer_graphe_3_coloriable(self):
        self.generer_couleurs()
        for i in range(self.nombre_de_noeuds):
            for j in range(i + 1, self.nombre_de_noeuds):
                if self.couleurs[i] != self.couleurs[j]:
                    # Vous pouvez choisir de relier ou non les nœuds avec une probabilité de 1/2
                    proba_relier = random.random()
                    if proba_relier < 0.5:
                        self.matrice_adjacence[i][j] = True
                        self.matrice_adjacence[j][i] = True

    def est_3_coloriable(self):
        # Vérifie si le graphe est 3-coloriable en parcourant les nœuds et en vérifiant les voisins
        for i in range(self.nombre_de_noeuds):
            for j in range(i + 1, self.nombre_de_noeuds):
                if self.matrice_adjacence[i][j] and self.couleurs[i] == self.couleurs[j]:
                    return False
        return True
    
    def dessinerGraphe(self, nom_fichier=None):
        # Créez un graphe vide
        G = nx.Graph()

        # Ajoutez les nœuds avec leurs couleurs
        for noeud, couleur in enumerate(self.couleurs):
            G.add_node(noeud, couleur=couleur)

        # Ajoutez les arêtes en fonction de la matrice d'adjacence
        for i in range(self.nombre_de_noeuds):
            for j in range(i + 1, self.nombre_de_noeuds):
                if self.matrice_adjacence[i][j]:
                    G.add_edge(i, j)

        # Positionnement des nœuds en forme de rond
        pos = nx.circular_layout(G)

        # Créez une liste de couleurs pour les nœuds en fonction de la couleur réelle
        couleurs_noeuds = [data['couleur'] for _, data in G.nodes(data=True)]

        # Définissez une liste de couleurs personnalisée correspondant à 'rouge', 'vert' et 'bleu'
        couleurs_personnalisees = {
            'rouge': 'red',
            'vert': 'green',
            'bleu': 'blue'
        }

        # Dessinez le graphe en utilisant les couleurs personnalisées
        nx.draw(G, pos, node_color=[couleurs_personnalisees[c] for c in couleurs_noeuds], with_labels=True, node_size=500)

        # Sauvegardez l'image au format PNG si un nom de fichier est spécifié
        if nom_fichier:
            plt.savefig(nom_fichier, format="png")

        # Affichez le graphique après la sauvegarde
        plt.show()


#main
if __name__ == "__main__":
    
    # Créez un graphe avec 10 nœuds
    graphe = Graphe(10)

    # Génère un graphe 3-coloriable
    graphe.generer_graphe_3_coloriable()
    
    # Vérifie si le graphe est 3-coloriable
    if graphe.est_3_coloriable():
        print("Le graphe est 3-coloriable.")
    else:
        print("Le graphe n'est pas 3-coloriable.")
    
    # Affiche la matrice d'adjacence et les couleurs
    print("Matrice d'adjacence:")
    for ligne in graphe.matrice_adjacence:
        print(ligne)
    
    print("Couleurs:")
    print(graphe.couleurs)
    
    # Dessine le graphe en forme de rond et sauvegarde en PNG
    graphe.dessinerGraphe(nom_fichier="graphe.png")