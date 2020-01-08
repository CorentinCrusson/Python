nombre = 0;

for i in range(100000000,1,-1):
	ok=0;
	for j in range(1,21):
		if i%j!=0:
			ok=1
			break;
	if(ok==0):
		nombre = i;
print(nombre)