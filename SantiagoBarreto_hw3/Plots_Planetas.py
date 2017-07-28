import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#codigo para animar el sistema solar, tomado de https://github.com/ComputoCienciasUniandes/Demonstrations/blob/master/SolarSystem/SolarSystem.ipynb

fig = plt.figure()
ax = p3.Axes3D(fig)
text = ax.text(-40, -30, 5, "")
fixed = [ax.plot(shorten[:, i, 0], shorten[:, i, 1], shorten[:, i, 2], c = colors[i]) for i in range(10)]
plots = [ax.plot([], [], [], "o", label = labels[i], color = colors[i])[0] for i in range(10)]
plots[0].set_marker("*")
plots[0].set_markersize(20)

ax.set_xlabel("$x$ (AU)")
ax.set_ylabel("$y$ (AU)")
ax.set_zlabel("$z$ (AU)")

plt.legend(numpoints=1)

def init():
    for (j, line) in enumerate(plots):
        line.set_data([], [])
        line.set_3d_properties([])
    text.set_text("")
    return plots, text

def update(i):
    for (j, line) in enumerate(plots):
        line.set_data(shorten[i, j, 0], shorten[i, j, 1])
        line.set_3d_properties(shorten[i, j, 2])
    time = i*dt*year_to_seconds*len(positions_in_time)/float(N) + init_time
    time = datetime.utcfromtimestamp(time)
    text.set_text(time.strftime('%Y-%m-%d'))
    return plots, text

ani = animation.FuncAnimation(fig, update, N)
#ani.save("Planets.gif", writer = "imagemagick", fps = N/30, dpi = 50)
plt.show()
