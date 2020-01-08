listePremier = [3];
i=0
while(len(listePremier)<10001):
	j = 2;
	ok = 0;
	while (j<100000 and ok==0):
		if i%j==0:
			ok=1;
		j+=1;
	if(ok==1):
		listePremier.append(i);
	i+=1
print(listePremier[10000])