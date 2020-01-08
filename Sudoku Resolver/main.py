from resolveMethods import *
from generateMethods import *

# Main
if __name__ == "__main__":
    # Déclaration de la grille en BRUTE
    """grille = [
        [0, 1, 9, 0, 5, 0, 0, 0, 0],
        [0, 4, 0, 0, 8, 3, 1, 0, 6],
        [6, 0, 0, 9, 0, 4, 0, 7, 0],
        [0, 0, 8, 1, 0, 0, 7, 3, 0],
        [0, 2, 0, 0, 7, 0, 0, 8, 0],
        [0, 7, 4, 0, 0, 6, 9, 0, 0],
        [0, 3, 0, 4, 0, 5, 0, 0, 7],
        [4, 0, 6, 7, 2, 0, 0, 5, 0],
        [0, 0, 0, 0, 6, 0, 4, 1, 0],
    ]"""
    sndGenerate(5)
    grille = setupGenerate(5)

    print("Génération d'une grille")

    afficheGrille(grille)

    resoudre(grille)

    afficheGrille(grille)

    """
    print("Lancement du Résolveur ...")

    resoudre(grille)

    afficheGrille(grille)
    print("Résolu ! ")
    """
