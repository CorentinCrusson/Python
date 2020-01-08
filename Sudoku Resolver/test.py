import random

liste1 = [0,1,2]
liste2 = [0,1,2]
#liste3 = liste1 * liste2
liste4 = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]


print("Lancement")
"""
for n in liste4:
    print(n[0])"""

X = random.sample(liste4,9)
for n in X:
    print(n)

print("fini")