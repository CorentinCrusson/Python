from resolveMethods import *
import random

# Setup parcours case par case
def setupGenerate(diff):
    grille = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    i = 2
    j = 2
    for a in range(1, 4):
        for b in range(1, 4):
            grille = generate(i * b, j * a, grille, diff)

    # Si la grille peut être résolute la renvoyer sinon la regénérer
    """if resoudre(grille):
        return grille
    else:
        setupGenerate(diff)
    """
    return grille

# Génération d'une Case
def generate(i, j, grille, diff):
    save = 0
    bx = (int)(i / 3)
    by = (int)(j / 3)
    liste4 = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    listey

    for tx in range(3):
        for ty in range(3):
            x = bx * 3 + tx
            y = by * 3 + ty

            L = random.sample(range(1, 10), 9)      
            
            if grille[x][y] != 0:
                continue
            for n in L:
                
                if checkLigne(grille, x, n) is True:
                    if checkColonne(grille, y, n) is True:
                        if checkCase(grille, x, y, n) is True:
                            grille[x][y] = n
                            save += 1
                            if save == diff:
                                return grille
                            break

    return grille