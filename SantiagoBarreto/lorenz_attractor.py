import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Defino el intervalo de tiempo en el que voy a evaluar las funciones, junto con el paso y el espacio en el que evaluare cada una de las variables

dt=0.01

min_t = 0.0

max_t = 40.0

n_points = int((max_t - min_t)/dt)

x = np.zeros(n_points)

y = np.zeros(n_points)

z = np.zeros(n_points)

#Defino las constantes

o=10.0

p=28.0

b=8.0/3.0

#Defino las 3 funciones que definen la derivada de cada una de las variables

def xt(x,y,z):
    dx = o * ( y - x )
    return dx

def yt(x,y,z):
    dy = ( x * ( p - z ) ) - y 
    return dy 

def zt(x,y,z):
    dz = ( x * y ) - ( b * z )
    return dz

#Declaro el intervalo de tiempo en el que se va a examinar

t = np.arange(min_t, max_t, dt)

#Valores iniciales

x[0] = 1.0
y[0] = 1.0
z[0] = 1.0

#Lleno los arreglos con los valores de las derivadas, recorriendo hacia adelante con el paso de Euler

for i in range(1,n_points):

    x[i] = x[i-1] + dt*xt(x[i-1],y[i-1],z[i-1])
    y[i] = y[i-1] + dt*yt(x[i-1],y[i-1],z[i-1])
    z[i] = z[i-1] + dt*zt(x[i-1],y[i-1],z[i-1])


fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(1,1,1, projection='3d')
ax.plot_wireframe(x,y,z,rstride=2)

plt.savefig("lorenz.png")
