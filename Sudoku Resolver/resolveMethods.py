# Grille Complete ou Non
def estComplete(grille):
    for i in range(9):
        if 0 in grille[i]:
            return False
    return True


# Ligne
def checkLigne(grille, i, num):
    vretour = True
    # t = ""
    for x in range(9):
        if grille[i][x] == num:
            vretour = False
        # t = t + " " if (x + 1) % 3 == 0 else t
    # print(t)
    return vretour


# Colonne
def checkColonne(grille, j, num):
    vretour = True
    # t = ""
    for y in range(9):
        if grille[y][j] == num:
            vretour = False
        # t = t + " " if (y + 1) % 3 == 0 else t
    return vretour


# Check Case v.2
def checkCase(grille, i, j, num):
    vretour = True

    bx = (int)(i / 3)
    by = (int)(j / 3)

    for x in range(3):
        for y in range(3):
            tx = bx * 3 + x
            ty = by * 3 + y
            if grille[tx][ty] == num:
                vretour = False

    return vretour


# Case
def checkCaseV1(grille, i, j, num):
    vretour = True
    numi = findCase(i)
    numj = findCase(j)

    # print("case " + str(i) + "," + str(j) + " : " + str(numi) + str(numj))

    for x in range(3):
        for y in range(3):
            if grille[numi + x][numj + y] == num:
                vretour = False

    return vretour


# Pour trouver dans quel case est le nbr
def findCase(nb):
    nbr = 0
    if nb % 2 == 0:
        if nb != 0:
            nbr = nb + (int(nb / 2) - 3)
            nbr = nbr - 3 if nb == 8 else nbr
    else:
        if (nb - 3 + 2) in [0, 6]:
            nbr = nb - 3 + 2
        else:
            if nb - 3 + 2 == 2:
                nbr = (nb - 3 + 2) + 1
            else:
                nbr = (nb - 3 + 2) - 1
    return nbr


# Afficher Grille
def afficheGrille(grille):
    for i in range(9):
        ligne = ""
        for j in range(9):
            ligne += str(grille[i][j])
            if j in [2, 5, 8]:
                ligne += "|"

        print(ligne + "\n")
        print("___|___|___|")


# Algo appellant les méthodes ci-dessus pour résoudre la grille donné en paramètre
# dans le main.py
def resoudre(grille):
    # Tant que la grille n'est pas complète
    while estComplete(grille) is False:

        # Ligne
        for i in range(9):

            # Colonne
            for j in range(9):

                # Si il y a déjà un chiffre
                if grille[i][j] != 0:
                    continue

                # Génération d'un chiffre pouvant être bon
                pos = []

                for k in range(1, 10):
                    # On passe tous les tests à notre nombre
                    if checkLigne(grille, i, k) is True:
                        if checkColonne(grille, j, k) is True:
                            if checkCase(grille, i, j, k) is True:
                                pos.append(k)
                    # Si trop de possibilités quitter la boucle
                    if len(pos) > 1:
                        break

                # Si on a qu'une seule possibilité alors HOP
                if len(pos) == 1:
                    grille[i][j] = pos[0]

                if estComplete(grille):
                    break
            if estComplete(grille):
                break
        if estComplete(grille) is False:
            nb = 0
            for n in range(0, len(grille)):
                nb += grille[n].count(0)
            print("Il manque " + str(nb) + " cases à remplir")
            return False
    return True
