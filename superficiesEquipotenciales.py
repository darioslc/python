import numpy as np
from numpy.polynomial import  Polynomial
import matplotlib.pyplot as plt


# valores de los puntos tomados en x e y para una misma superficie equipotencial
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 7.5, 8, 8.7, 8.6]
y1 = [11.1, 11, 10.7, 10.1, 9.5, 9, 8, 7, 6, 5.2, 2, 1]

# misma lista pero convertida a metros
x1 = list(map(lambda x: x / 100, x1))
y1 = list(map(lambda x: x / 100, y1))

fig, ax = plt.subplots()

plt.rcParams['text.usetex'] = True

# ajuste a polinomio de grado 2, "y" es la variable independiente en este caso. El ajuste puede ser otro tipo de función o polinomio, por lo que puede no ser un polinomio de grado 2, dependerá de la configuración.
polinomio = Polynomial.fit(y1, x1, 2, domain=[min(y1), max(y1)])
print(polinomio)
fit_y, fit_x = polinomio.linspace(100)
plt.plot(fit_x, fit_y, color="tab:red")
plt.plot(x1, y1, 'o', color="tab:red", label="V")


plt.plot(-6.5, 3.5, "+", color="red", markersize=15)
plt.plot(4.5, 5.5, "_", color="red", markersize=15)

ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set(xlim=(min(x1)-.1, max(x1)+.1))
ax.set(ylim=(min(y1)-.1, max(y1)+.1))
ax.set_aspect('equal')
ax.legend(bbox_to_anchor=(1.25, 0.7))

# =============================================================================
# In[acá se puede hacer un esquema de la configuración de electrodos]
# =============================================================================
# hace líneas verticales y horizontales
#plt.vlines(-.1, -.1, .1, colors="black", lw=5)
#plt.hlines(.1, -.1, -.05, colors="black", lw=5)

# si es un cuarto de circunferencia
radio = .1
x = np.linspace(0, radio)
plt.plot(x, np.sqrt(radio**2-(x+.05)**2)-0.05,)

plt.grid()
plt.show()

# =============================================================================
# In[con una función] 
# =============================================================================
def datos_ajuste_graf(x,y,colores):
#    x = list(map(lambda x: x / 100, x1))
#    y = list(map(lambda x: x / 100, y1))
    
    plt.rcParams['text.usetex'] = True
    
    polinomio = Polynomial.fit(y, x, 2, domain=[min(y), max(y)])
    print(polinomio)
    fit_y, fit_x = polinomio.linspace(100)
    plt.plot(fit_x, fit_y, color=colores)
    plt.plot(x, y, 'o', color=colores, label="V")

    plt.plot(-6.5, 3.5, "+", color=colores, markersize=15)
    plt.plot(4.5, 5.5, "_", color=colores, markersize=15)

    plt.xlabel('$x$ [m]')
    plt.ylabel('$y$ [m]')    

# ============================================================================
# In[pruebas]
# =============================================================================
# V = 2.2 V
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 7.5, 8, 8.7, 8.6]
y1 = [11.1, 11, 10.7, 10.1, 9.5, 9, 8, 7, 6, 5.2, 2, 1]
# V = 2.5 V
x2 = [10, 9.8, 9.5, 9, 8.3, 8, 7, 6, 5, 4, 3]
y2 = [1, 1.9, 3, 4.5, 6.4, 7, 8.3, 9.3, 9.9, 10.6, 11]

# colores = b-blue, c-cyan,g-green,k-black,m-magenta,r-red,w,white,y-yellow 
colores = ['b', 'c', 'g', 'k', 'm', 'r', 'w', 'y']
colores[0] == 'b' 
datos_ajuste_graf(x2, y2,colores[7])
datos_ajuste_graf(x1,y1,colores[2])

# hace líneas verticales y horizontales
#plt.vlines(-.1, -.1, .1, colors="black", lw=5)
#plt.hlines(.1, -.1, -.05, colors="black", lw=5)

# si es un cuarto de circunferencia
#radio = .1
#xc = np.linspace(0, radio)
#plt.plot(xc, np.sqrt(radio**2-(xc+.05)**2)-0.05,)

plt.title("AÑADIR TTITULO")
plt.grid()
plt.show()
