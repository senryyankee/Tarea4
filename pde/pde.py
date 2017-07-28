import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

n_points = 1000
x = np.linspace(0.0,1.0,n_points)
u_initial = np.exp(-((x-0.3)*(x-0.3))/0.01)



delta_x = x[1]-x[0]
delta_t = 0.0005
c = 1.0
r = c * delta_t / delta_x

u_initial[0] = 0.0
u_initial[n_points-1] = 0.0

u_future = np.zeros(n_points)
u_future[0] = 0.0
u_future[n_points-1] = 0.0

for i in range(1,n_points-1):
    u_future[i] = u_initial[i] + (r**2/2.0) * (u_initial[i+1] - 2.0 * u_initial[i] + u_initial[i-1])

#create a new variable to hold the previous value
u_past = u_initial.copy()
#create a new variable to hold the present value
u_present = u_future.copy()

n_time = 350
for j in range(n_time):
    for i in range(1,n_points-1):
        u_future[i] = (2.0*(1.0-r**2))*u_present[i] - u_past[i] + (r**2)*(u_present[i+1] +  u_present[i-1])
    u_past = u_present.copy()
    #create a new variable to hold the present value
    u_present = u_future.copy()

#plt.plot(x, u_initial)
plt.plot(x, u_past)
plt.plot(x, u_present)
plt.show()
plt.close()












