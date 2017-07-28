a=16
b=32

if a % 2 == 0:
	print("a es par")
else: 
	print("a es impar")

divisores=[]
for x in range(1, a+1):
	if a % x == 0:
		divisores.append(x)
print("Los divisores de a son",divisores)


maximo=[]
if a < b:
	for z in range(1, a+1):
		if (a % z == 0 and b % z == 0):
			maximo.append(z)
	print(maximo[-1])
if a > b:
	for z in range(1, b+1):
		if (a % z == 0 and b % z == 0):
			maximo.append(z)
	print(maximo[-1])

