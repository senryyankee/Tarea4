import numpy as np 
import matplotlib.pylab as plt
from matplotlib import animation

#La estructura general del codigo esta basada en forma no literal de ejemplos de semestres pasados disponibles en https://github.com/ComputoCienciasUniandes/MetodosComputacionales/tree/master/slides/2015-V y la definicion de funciones sacada de http://hplgit.github.io/INF5620/doc/notes/wave-sphinx/main_wave.html

#Asi mismo tambien se tomaron elementos de la clase de laboratorio donde se resuelve una ecuacion de onda en 1D, y del github https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/11.PDEs/PDE.ipynb

#Tambien fue tomada en cuenta la solucion del Landau para la ecuacion de onda

#Se escogen valores de x y y para que la onda se origine en un tercio de la parte de arriba y en el centro
izq = -15.0  
der = 15.0   
bot = -10.0
top = 20.0

#Se escoge un valor tal que la grilla tenga 300 espacios y se definen los limites de la grilla
l = 300
dx = ( der - izq ) / l
dy = ( top - bot ) / l

#Defino constantes

v=1.0 #Velocidad de la onda, c
r=0.5 #Constante gama
dt=np.sqrt(r)*dx/v #El paso del tiempo se define como la raiz cuadrada de gamma divido en la velocidad de la onda

#Tiempos a examinar
t_1=30.0 #Tiempo 1
t_f=60.0 #Tiempo final

#El paso de cada uno de los tiempos se da en funcion de la division entre el paso del tiempo en general

Pt_1 = int( t_1 / dt)
Pt_f = int( t_f / dt)

#Defino el espacio

x = np.linspace( izq, der, l )
y = np.linspace( bot, top, l )

#Se utiliza el metodo de numpy meshgrid para crear la grilla
x_grilla , y_grilla = np.meshgrid( x , y )

#defino la funcion que genera el frente de onda 

def f_onda (arg) :
	onda = np.zeros(( arg , l , l ))
	ancho = 0.3
	#Condicion inicial de la onda en ambas dimensiones
	onda[0] = (-0.5)*np.exp(-x_grilla**2/(2*ancho**2))*np.exp(-y_grilla**2/(2*ancho**2))
	#Metodo roll para que la onda recorra el arreglo
	onda[1] = onda[0] + r**2/2.*(np.roll(onda[0],1,axis=0)+np.roll(onda[0],-1,axis=0)+np.roll(onda[0],1,axis=1)+np.roll(onda[0],-1,axis=1)-4*onda[0])
	#Condiciones iniciales
	onda[0,0] = 0
	onda[0,-1] = 0
	onda[1,:,0] = 0
	onda[1,:,-1] = 0
	#Se crean arreglos que modifican la onda
	for i in range(2,arg):
		parcial = onda[i-1]
		ppar = onda[i-2]
		onda[i]=2*(1.-2.*r**2)*parcial-ppar+r**2*(np.roll(parcial,1,axis=1)+np.roll(parcial,-1,axis=1)+np.roll(parcial,1,axis=0)+np.roll(parcial,-1,axis=0))
		onda[i,0:2]=2.0    
	return onda

#grafico la condicion en el tiempo final

tiempof = f_onda(Pt_f)
fig=plt.figure(figsize=(10,10))
plt.imshow(abs(tiempof[tiempof.shape[0]-1]),cmap="hot",extent=(izq+dx,der-dx,bot+dy,top-dy))
nivel = plt.colorbar()
plt.xlabel('X, 30 unidades')
plt.ylabel('Y, 30 unidades')
plt.title('Onda propagada')
nivel.ax.set_xlabel('Profundidad')
plt.savefig('t_f.png')
plt.close()

#Grafico la condicion en el tiempo 30

tiempo1 = f_onda(Pt_1)
fig=plt.figure(figsize=(10,10))
plt.imshow(abs(tiempo1[tiempo1.shape[0]-1]),cmap="hot",extent=(izq+dx,der-dx,bot+dy,top-dy))
nivel = plt.colorbar()
plt.xlabel('X, 30 unidades')
plt.ylabel('Y, 30 unidades')
plt.title('Onda propagada')
nivel.ax.set_xlabel('Profundidad')
plt.savefig('t_1.png')
plt.close()

#Animacion

fig=plt.figure(figsize=(10,10))
p=plt.imshow(abs(tiempo1[0]),cmap="hot",extent=(izq+dx,der-dx,bot+dy,top-dy))
nivel = plt.colorbar()
plt.xlabel('X, 30 unidades')
plt.ylabel('Y, 30 unidades')
plt.title('Onda propagada')
nivel.ax.set_xlabel('Profundidad')

def animate(i):
	p.set_array(abs(tiempof[i]))
	return p,
peli = animation.FuncAnimation(fig, animate, np.arange(1,len(tiempof)),interval=20, blit=False)

peli.save('Onda.mp4', bitrate=512)








