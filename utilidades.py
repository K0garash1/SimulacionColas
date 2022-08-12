import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Margen de error
z_score = 0.05

#Generador de datos

def obtenerDistibucionNormal(u, s, n):
    array = np.random.normal(u, s, n)
    return array

def obtenerDistibucionPoisson(l, n):
    array = np.random.poisson(l, n)
    return array

#Test de Kolmogorov–Smirnov

def testNorm(dist, u, s):
    s, p = stats.kstest(dist, stats.norm.rvs(loc=u, scale=s, size=100000))
    print(f">> El valor Z para la pueba es {p}")
    if p < z_score:
        print(f">> Se rechaza la hipoteseis nula (puntaje z menor a {z_score})")
    else:
        print(f">> No se puede rechazar la hipotesis nula (puntaje z mayor o igual a {z_score})")

def testPoisson(dist, l):
    s, p = stats.kstest(dist, stats.poisson.rvs(mu= l, size=100000))
    print(f">> El valor Z para la pueba es {p}")
    if p < z_score:
        print(f">> Se rechaza la hipoteseis nula (puntaje z menor a {z_score})")
    else:
        print(f">> No se puede rechazar la hipotesis nula (puntaje z mayor o igual a {z_score})")

#Grafica histograma de un arreglo de datos
def graficarDistribucion(dist, titulo, u, s):
    plt.hist(dist, density=True)
    x = np.linspace(0,30, 100)
    if s == 0:
        plt.plot(x, stats.poisson.pmf(x, u, s))
    else:
        plt.plot(x, stats.norm.pdf(x, u, s))
    plt.title(titulo)
    plt.show()

#Grafica lista de datos
def graficarLista(lista, titulo):
    plt.plot(lista)
    plt.title(titulo)
    plt.show()

#Acumula los tiempos de una lista
def acumular(lista):
    respuesta = []
    acumulado = 0
    for i in range(0, len(lista)):
        acumulado+=lista[i]
        respuesta.append(acumulado)
    return respuesta

#Promedio de una lista
def promedio(lista):
    promedio = 0
    for i in range(0, len(lista)):
        promedio+=lista[i]
    return promedio/len(lista)