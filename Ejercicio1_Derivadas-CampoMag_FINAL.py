import numpy as np
import matplotlib.pyplot as plt

#Complementaria: TALLER 2 
#Ejercicio #1: Derivadas y campo magnético

#PUNTO 1 (teórico): Subido como pdf


#PUNTO 2: Gráfica de corriente
#Estableciendo parámetros dados
B = 0.05
w = 3.5
f = 7
R = 1750
r = 0.25/2

t = np.linspace(0, 1.8, 1000)
h = t[1]-t[0]
I=[]

#Estableciendo phi 
phi = (np.pi*r**2)*(B)*np.cos(w*t)*np.cos(2*np.pi*f*t)

#Derivada inicial (derecha)
I.append(-1/R*(phi[1]-phi[0])/(2*h))

#Derivadas intermedias (central)
for i in range(1,len(t)-1):
    a = -1/R*(phi[i+1]-phi[i-1])/(2*h)
    I.append(a)
    
#Derivada final (izquierda)
I.append(-1/R*(phi[len(t)-1]-phi[len(t)-2])/(2*h))
plt.plot(t, I)
plt.title("Corriente vs Tiempo")
plt.grid()
plt.show()
#plt.plot(t, phi)







#PUNTO 3: Hallar primeras 3 raíces
#Utilizando Newton Raphson para hallar raices 
def Funcion(x):
    return 40*(np.pi*r**2)*(B)*np.cos(w*x)*np.cos(2*np.pi*f*x)

x = np.linspace(0,0.0015,100)
y = Funcion(x)

#Hallar derivada
def derivada(funcion, x, h=1e-10):
    d=0.
    if h!=0:
        d=(funcion(x+h)-funcion(x-h))/(2*h) 
        return d 


#aplicando metodo (halla una raiz para un xi dado)
def NewtonRaphson(xi):
    #parametros Iniciales
    fxi = Funcion(xi)
    dxi = derivada(Funcion, xi)
    for i in range(50): 
        x = xi - (fxi/dxi)
        fxi = Funcion(x)
        dxi = derivada(Funcion, x) 
        xi = x 
    return x


#hallando todas las raices
def GetAllRoots(x,Funcion):
    Roots = []
    for i in x:
        root = NewtonRaphson(i)
        root = np.round(root,10) 
        Roots.append(root)
        
    unique_roots = [] 
    for i in Roots:

        if i not in unique_roots and i>=0:
            unique_roots.append(i)
    unique_roots.sort()
    return unique_roots
 

print("las primeras 3 raices son: ", GetAllRoots(x, Funcion)[:3])