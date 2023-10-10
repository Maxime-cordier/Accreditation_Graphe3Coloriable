import random
import matplotlib.pyplot as plt
import networkx as nx
import hashlib

NOMBRE_NOEUD = 20

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
        #plt.show()
    
    def miseEnGageColoriage(self, valeurs_aleatoires):
        mises_en_gage = []

        for i in range(self.nombre_de_noeuds):
            couleur = self.couleurs[i]
            valeur_aleatoire = valeurs_aleatoires[i]

            # Convertissez la couleur en une chaîne d'octets (UTF-8)
            couleur_bytes = couleur.encode('utf-8')

            # Concaténez la couleur et la valeur aléatoire
            couleur_concatenee = couleur_bytes + valeur_aleatoire.to_bytes(16, byteorder='big')
            #print(couleur_concatenee)

            # Appliquez la fonction de hachage SHA-1
            h = hashlib.sha1()
            h.update(couleur_concatenee)
            mise_en_gage = h.digest()

            mises_en_gage.append(mise_en_gage.hex())

        return mises_en_gage

    def preuveColoriage(self, i, j, Ti, Tj,mise_en_gage_i, mise_en_gage_j):
        # Vérifiez que les couleurs des nœuds i et j sont différentes

        if self.couleurs[i] == self.couleurs[j]:
            print("Les couleurs des nœuds i et j sont les mêmes.")
            return False
        
        couleur_i = Ti[0].encode('utf-8')
        couleur_j = Tj[0].encode('utf-8')
        valeur_aleatoire_i = Ti[1]
        valeur_aleatoire_j = Tj[1]

        concatenation_i = couleur_i + valeur_aleatoire_i.to_bytes(16, byteorder='big')
        concatenation_j = couleur_j + valeur_aleatoire_j.to_bytes(16, byteorder='big')

        # Calculez les hachages SHA-1 correspondants
        h_ri_ci = hashlib.sha1(concatenation_i).digest()
        h_rj_cj = hashlib.sha1(concatenation_j).digest()

        print("Hashage_i_verifieur : "+str(h_ri_ci.hex()))
        print("Hashage_j_verifieur : "+str(h_rj_cj.hex()))

        # Vérifiez si h(ri || ci) = yi et h(rj || cj) = yjmain.py
        if (h_ri_ci.hex() == mise_en_gage_i) and (h_rj_cj.hex() == mise_en_gage_j):
            return True
        else:
            return False



#main
if __name__ == "__main__":
    
    # Créez un graphe avec 10 nœuds
    graphe = Graphe(NOMBRE_NOEUD)

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
    
    # permuter aléatoirement les couleurs les vert en bleu ou rouge. Les bleu en vert ou rouge. Les rouge en vert ou bleu
    couleurs_set_rouge = ""
    couleurs_set_vert = ""
    couleurs_set_bleu = ""
    
    couleurs_set_rouge = random.choice(["vert", "bleu"])
    if couleurs_set_rouge == "bleu":
        couleurs_set_vert = "rouge"
        couleurs_set_bleu = "vert"
    else:
        couleurs_set_vert = "bleu"
        couleurs_set_bleu = "rouge"

    new_couleurs = []
    for couleur in graphe.couleurs:
        if couleur == "rouge":
            new_couleurs.append(couleurs_set_rouge)
        elif couleur == "vert":
            new_couleurs.append(couleurs_set_vert)
        else:
            new_couleurs.append(couleurs_set_bleu)

    graphe.couleurs = new_couleurs

    print(graphe.couleurs)
    graphe.dessinerGraphe(nom_fichier="graphe_permute.png")

    # Génère des valeurs aléatoires de 128 bits pour la mise en gage
    valeurs_aleatoires = [random.randint(0, 2**128 - 1) for _ in range(graphe.nombre_de_noeuds)]

    # Calcule les valeurs de mise en gage des couleurs
    mises_en_gage = graphe.miseEnGageColoriage(valeurs_aleatoires)
    print(mises_en_gage)
    print("Mises en gage des couleurs:")
    for i, mise_en_gage in enumerate(mises_en_gage):
        print(f"Nœud {i+1}: {mise_en_gage}")

    # Répétez le protocole de preuve 400 fois
    nombre_de_tests = 400
    reussites = 0
    a=0

    while(a<nombre_de_tests):
        i, j = random.sample(range(graphe.nombre_de_noeuds), 2)
        if (graphe.matrice_adjacence[i][j] == True):

            print("Arrete entre "+str(i)+" et "+str(j))

            a=a+1
            mise_en_gage_i = mises_en_gage[i]
            mise_en_gage_j = mises_en_gage[j]

            print("Hashage_i_prouveur : "+str(mise_en_gage_i))
            print("Hashage_j_prouveur : "+str(mise_en_gage_j))

            if graphe.preuveColoriage(i, j, (graphe.couleurs[i], valeurs_aleatoires[i]), (graphe.couleurs[j], valeurs_aleatoires[j]), mise_en_gage_i, mise_en_gage_j):
                reussites += 1
                print("reussites : "+str(reussites))
            else : 
                print("Echec")
        else:
            print("Pas d'arrete entre "+str(i)+" et "+str(j))
            
    print("Nombre de tests réussis:", reussites)
    print("Nombre de tests:", nombre_de_tests)
    if reussites == nombre_de_tests:
        print("L'utilisateur est authentifié.")
    else:
        print("L'utilisateur n'est pas authentifié.")