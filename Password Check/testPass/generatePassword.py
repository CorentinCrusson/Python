# -*- coding: cp1252 -*-
 
import string
from random import sample
 
# lettres min + lettres maj + chiffres
pop = string.ascii_letters + string.punctuation + string.digits
# le mot de passe fera 12 caractères de long
k=6
 
# sample retourne une portion aléatoire et de taille k à partir de la séquence pop
passwd = ''.join( sample(pop, k) )
print(pop)
print(passwd)

""" 
print("==========================================")
#la seule restriction ici c'est que k ne peut pas être supérieur
# à la taille de la population, si tu veux un mdp plus long, il faut agrandir
# la population, d'une manière ou d'une autre :
 
k=200
 
# exemple simple
while k > len(pop):
    pop *= 2
     
passwd = ''.join(sample(pop, k))
     
print(pop)
print(passwd)
"""