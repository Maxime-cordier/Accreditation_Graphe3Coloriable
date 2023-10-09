import graphe3Coloriable

# =========== Première étape : Génération du graphe ===========

# Créer un nouveau graphe 3-coloriable avec 10 nœuds
graphe = graphe3Coloriable.Graphe3Coloriable(9)

# Dessiner le graphe
graphe.dessiner()

# =========== Deuxième étape : Recoloriage du graphe ===========

# Recolorier le graphe pour assurer que le graphe ne soit pas connu
graphe.recolorier()

# Dessiner le graphe
graphe.dessiner()

# =========== Troisième étape : Recoloriage du graphe ===========