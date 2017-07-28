texto = open('pg1524.txt')


lineas = texto.readlines()

palabras=[]

for x in lineas:
	palabras.extend(x.split())

#print(palabras)
numeros=[]
for n in range(1,10):	
	i=0
	for y in palabras:
		if len(y)==n:
			i=i+1
	numeros.append(i)
print(numeros)

