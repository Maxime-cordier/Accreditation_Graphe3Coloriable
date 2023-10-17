# Graphe 3-Coloriable et Protocole de Preuve à Divulgation Nulle

## Description

Ce programme génère un graphe aléatoire et le colore de manière à ce qu'il soit 3-coloriable. Il implémente ensuite un protocole de preuve à divulgation nulle pour vérifier que le graphe est effectivement 3-coloriable, sans révéler le coloriage spécifique du graphe au vérificateur. Le programme utilise des techniques de cryptographie pour créer une mise en gage des couleurs, permettant ainsi une vérification sûre et confidentielle.

## Fonctionnalités

- Génère un graphe aléatoire 3-coloriable avec un nombre spécifié de nœuds.
- Permet de visualiser le graphe et son coloriage.
- Effectue un protocole de preuve à divulgation nulle pour vérifier la 3-coloriabilité du graphe.
- Utilise des hachages SHA-1 pour créer des mises en gage des couleurs des nœuds.
- Effectue plusieurs tests pour s'assurer de la validité du protocole.

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

- `networkx`
- `matplotlib`
- `hashlib`
- `random`

Vous pouvez les installer via pip :

```bash
pip install networkx matplotlib
```

## Utilisation
1. Clonez ce dépôt sur votre machine locale.
2. Naviguez dans le dossier contenant le script Python.
3. Exécutez le script avec la commande :

```bash
python main.py
```
## Aperçu du code
Le programme contient une classe Graphe qui est responsable de la création et de la gestion du graphe. Elle contient plusieurs méthodes, y compris pour générer le graphe, pour vérifier s'il est 3-coloriable, pour dessiner le graphe et pour exécuter le protocole de preuve.

## Auteurs

[Maxime CORDIER](https://github.com/Maxime-cordier)

[Sylvain MESTRE](https://github.com/Shult)
