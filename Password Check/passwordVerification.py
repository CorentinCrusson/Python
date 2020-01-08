import re


def haveDigit(word):
    for letter in word:
        if letter in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return True
    return False


def haveSpecialCharacter(word):
    for letter in word:
        if letter in ('`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', '\\', ': ', ',''', '<', ',', '>', '.', '?', '/'):
            return True
    return False


def dicoAttack(password):
    filepath = 'dictionnary.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if(line == password):
                return True
            line = fp.readline()
    return False


def checkingPass(password):
    # Mot de passe supérieur ou égale à 6 caractères
    if(len(password) >= 6):
        # Caractère Spécial First
        if (haveSpecialCharacter(password)):
            if(re.match('[A-Z]+', password)):
                if(haveDigit(password)):
                    if (len(password) > 8):
                        comment = ""
                        level = "PERFECT"
                    else:
                        comment = "Bon mot de passe"
                        level = "GOOD"
                else:
                    comment = "Le mot de passe manque d'un chiffre"
                    level = "MEDIUM"
            else:
                if(haveDigit(password)):
                    comment = "Le mot de passe manque d'une majuscule"
                    level = "MEDIUM"
                else:
                    comment = "Le mot de passe manque d'un chiffre et d'une majuscule"
                    level = "BAD"
                    # Majuscule First
        elif(re.match('[A-Z]+', password)):
            if(haveDigit(password)):
                comment = "Le mot de passe manque d'un caractère spécial"
                level = "MEDIUM"
            else:
                comment = "Le mot de passe manque d'un chiffre et d'un caractère spécial"
                level = "BAD"

        # Chiffre first
        else:
            if(haveDigit(password)):
                comment = "Le mot de passe manque d'une majuscule et d'un caractère spécial"
                level = "BAD"
            else:
                comment = "Le mot de passe manque d'une majuscule, d'un caractère spécial et d'un chiffre"
                level = "VERY BAD"

    # Inférieur à 6 caractères
    else:
        comment = "Le mot de passe doit faire minimum 6 caractères et non " + \
            str(len(password))+"caractères !"
        level = "VERY BAD"

    if(dicoAttack(password)):
        comment = "Le mot de passe est déjà connu"
        level = "VERY BAD"

    return level, comment
