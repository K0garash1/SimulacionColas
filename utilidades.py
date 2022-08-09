import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

z_score = 0.05

def obtenerDistibucionNormal(u, s, n):
    array = np.random.normal(u, s, n)
    return array

def obtenerDistibucionPoisson(l, n):
    array = stats.poisson.rvs(size=n, mu = l)
    #array = np.random.poisson(l, n)
    return array

def graficarDistribucion(dist):
    plt.hist(dist, density=True)
    plt.show()

def testNorm(dist, u, s):
    s, p = stats.kstest(dist, 'norm', args=(u, s))
    print(f"> El valor Z para la pueba es {p}")
    if p < z_score:
        print(f">> Se rechaza la hipoteseis nula (puntaje z menor a {z_score})")
    else:
        print(f">> No se puede rechazar la hipotesis nula (puntaje z mayor o igual a {z_score})")

def testPoisson(dist, l):
    s, p = stats.kstest(dist, stats.poisson.rvs(mu= l, size=10000))
    print(f"> El valor Z para la pueba es {p}")
    if p < z_score:
        print(f">> Se rechaza la hipoteseis nula (puntaje z menor a {z_score})")
    else:
        print(f">> No se puede rechazar la hipotesis nula (puntaje z mayor o igual a {z_score})")
    