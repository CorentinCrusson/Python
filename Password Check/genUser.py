import string
from random import sample,randint

def lengthOfFile(filepath):
    length = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            length += 1
            line = fp.readline()
    return length

def randomPickInFile(filepath,len):

    i = randint(1,len)
    j = 0

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            j += 1
            if j==i:
                return line.replace('\n','')

            line = fp.readline()
    

    return 'ErR0r'

def generatePassword(filepath,len):

    # Password Generate avec une probabilité de 4/5
    if (randint(0,5)!=0):
        # String to enable a generate
        pop = string.ascii_letters
        if(randint(0,1)==0):
            pop = pop + string.digits
        
        if(randint(0,3)==0):
            pop = pop + string.punctuation

        # Password Length
        k=randint(3,12)

        # sample retourne une portion aléatoire et de taille k à partir de la séquence pop
        passwd = ''.join( sample(pop, k) )
        #print(pop)
    else:
        passwd = randomPickInFile(filepath,len)

    return passwd

def generateUser(files):
    lstReturn = []
    for f in files:
        if f[0]=='dictionnary.txt':
            lstReturn.append(generatePassword(f[0],f[1]))
        else:
            lstReturn.append(randomPickInFile(f[0],f[1]))  
    return lstReturn
