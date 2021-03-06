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


def haveUpperCase(word):
    for letter in word:
        if(re.match('[A-Z]', letter)):
            return True
    return False


def dicoAttack(password):
    i = 0
    filepath = 'dictionnary.txt'
    with open(filepath) as fp:
        line = fp.readline()
        if(line == password+"\n"):
            return True
        line = fp.readline()
    
    return False

def checkingPass(password):

    # Mot de passe supérieur ou égale à 8 caractères
    if(len(password) >= 8):

        # Caractère Spécial First
        if (haveSpecialCharacter(password)):
            if(haveUpperCase(password)):
                if(haveDigit(password)):
                    if (len(password) > 10):
                        comment = ""
                        level = "PERFECT"
                    else:
                        comment = "Bon mot de passe"
                        level = "GOOD"
                else:
                    comment = " manque d'un chiffre"
                    level = "MEDIUM"
            else:
                if(haveDigit(password)):
                    comment = " manque d'une majuscule"
                    level = "MEDIUM"
                else:
                    comment = " manque d'un chiffre et d'une majuscule"
                    level = "BAD"
                    # Majuscule First
        elif(haveUpperCase(password)):
            if(haveDigit(password)):
                comment = " manque d'un caractère spécial"
                level = "MEDIUM"
            else:
                comment = " manque d'un chiffre et d'un caractère spécial"
                level = "BAD"

        # Chiffre first
        else:
            if(haveDigit(password)):
                comment = " manque d'une majuscule et d'un caractère spécial"
                level = "BAD"
            else:
                comment = " manque d'une majuscule, d'un caractère spécial et d'un chiffre"
                level = "VERY BAD"

    # Inférieur à 7 caractères
    else:
        comment = " doit faire minimum 8 caractères et non " + \
            str(len(password))+" caractères !"
        level = "VERY BAD"

    if(dicoAttack(password)):
        comment = " est déjà connu"
        level = "VERY BAD"

    # On évite la répitition
    if(level in ['VERY BAD', 'BAD', 'MEDIUM']):

        comment = "Le mot de passe"+comment

    if level != 'PERFECT':
        comment = " : "+comment

    return level, comment
