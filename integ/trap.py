a = 0.0
b = 3.0
N = 1000000


def f(y):
	return y*y


def wTrap(i, h):

	if ((i == 1) or (i ==N)):
		wLocal=h/2.0
	
	else:
		wLocal = h
	
	return wLocal


h = (b - a)/(N - 1)


suma= 0.0


for i in range (1, N+1):

	t= a + (i-1)*h

	w=wTrap(i, h)

	suma = suma + w*f(t)



print '\n Final sum=', suma

print "Press a character to finish"

s=raw_input()
