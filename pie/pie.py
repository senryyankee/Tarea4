import numpy as np
import matplotlib.pyplot as plt
import math
import random



h = 0.01
n_points = int(6.0/h)
x = np.linspace(-1.0,1.0,n_points)
y=np.sqrt(1 - (x*x))

integral = sum(y) * h

print integral

plt.bar(x,y, width=h)
plt.show()
plt.close()
