import random
import matplotlib.pyplot as plt
import networkx as nx

class Graphe3Coloriable:
    def __init__(self, n):
        self.n = n  # Nombre total de noeuds
        self.G = nx.Graph()
        self.couleurs = ["red"] * (n//3) + ["green"] * (n//3) + ["blue"] * (n//3 + n % 3)

        # Assurons que le graphe est 3-coloriable
        for i, couleur in enumerate(self.couleurs):
            self.G.add_node(i, color=couleur)

        for i in range(n):
            for j in range(i+1, n):
                if self.couleurs[i] != self.couleurs[j]:
                    self.G.add_edge(i, j)

    def dessiner(self):
        couleurs = [self.G.nodes[i]["color"] for i in self.G.nodes]
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color=couleurs, node_size=800)
        plt.show()

    def recolorier(self):
        # Définir toutes les couleurs à rouge
        for i in self.G.nodes:
            self.G.nodes[i]["color"] = "red"

        # Recolorier pour assurer un graphe 3-coloriable
        for i, couleur in enumerate(self.couleurs):
            voisins = self.G[i]
            couleurs_voisins = {self.G.nodes[j]["color"] for j in voisins}

            # Choix des couleurs disponibles
            choix_couleurs = {"red", "green", "blue"} - couleurs_voisins

            # Recolorier le nœud
            self.G.nodes[i]["color"] = choix_couleurs.pop()

# Test
# graphe = Graphe3Coloriable(9)
# graphe.dessiner()

# graphe.recolorier()
# graphe.dessiner()