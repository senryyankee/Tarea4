import numpy as np 
import matplotlib.pyplot as plt

#Defino las condiciones iniciales 

xi = 0.0
yi = 0.0
vxi = 0.0
vyi = 5.0 
g= 9.8

#Defino el tiempo
nt=100000
t = np.linspace(0,1.5, nt)

def posicion(xi, vi, t):
		
	x= xi + vi*t - (0.5)*g*t*t
	
	return x

x= posicion(yi, vyi, t)


def velocidad(vi,t):

	v=vi - g*t
	return v

v= velocidad(vyi,t)

plt.plot(t,x)
plt.savefig("posBalon.pdf")
plt.close()

plt.plot(t,v)
plt.savefig("velBalon.pdf")
plt.close

xm=np.amax(x)
print "La altura maxima alcanzada es", xm, "metros."

pos=0

for i in range(nt+1):
	if (x[i-1]>0 and x[i]<0):
		pos=i-1
	
print "Tiempo del balon en el aire:",  t[pos], "segundos."
	







