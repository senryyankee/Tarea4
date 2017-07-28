import numpy as np
import matplotlib.pyplot as plt

#Defino funcion

def f(x):
	return x*x

#Derivada por backward

def derivar(f,x):
	h= x[2]-x[1]
	df = (f[2:]-f[0:-2])/(2*h)
	dx = x[1:-1]
	return(df,dx)

#Derivada por forward

def fd (f,x):
	h= x[2]-x[1]
	o= (x[2]-x[1])/2
	df = (f[1:]-f[0:-1])/(h)
	dx = x[1:]
	return(df,dx)

#Derivada por Central

def cd (f,x):
	h= (x[2]-x[1])/2
	df = ((f[1:])-(f[0:-1]))/(2*h)
	dx = x[:-1]
	return(df,dx)
	

#Derivada extrapolation

def ed (f,x):
	h= (x[2]-x[1])
	df = ((((f[1:])-(f[0:-1]))/(h))*(4/3))-((((f[1:])-(f[0:-1]))/(h))*(1/3))
	dx = x[:-1]
	return(df,dx)	

#Errores




#Defino variables



x = np.linspace(-10.0,10.0,1000)
g=f(x)
df,dx=derivar(g,x)
ff,xx=fd(g,x)
cc,cx=cd(g,x)
ee,ex=ed(g,x)

#Grafico

plt.plot(x,g)
#plt.plot(xx,ff)
#plt.plot(dx,df)
plt.plot(cx,cc)
#plt.plot(ex,ee)
plt.show()
plt.close()
	
	
