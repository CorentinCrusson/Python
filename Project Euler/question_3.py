somme = 0
listePremier = [3];

for i in range(3,7000):
	j = 2;
	ok = 0;
	while (j<7000 and ok==0):
		if i%j==0:
			ok=1;
		j+=1;
	print("coucou")
	if(ok==1):
		listePremier.append(i);

number = int(input("Le nombre : "));
leMax = 0;
for nombre in listePremier:
	if(number%nombre==0):
		leMax = nombre
print(leMax)