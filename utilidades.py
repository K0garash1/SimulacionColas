import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def obtenerDistibucion(u, s, n):
    array = np.random.normal(u, s, n)
    return array

def graficarDistribucion(dist):
    plt.hist(dist, density=True)
    plt.show()

def testNormal(dist):
    k, p = stats.normaltest(dist)
    # F. J. Anscombe, W. J. Glynn, “Distribution of the kurtosis statistic b2 for normal samples”, Biometrika, vol. 70, pp. 227-234, 1983.
    print(f"El valor Z para la pueba de curtosis es {p}")
    if p< 1e-3:
        print("Se rechaza la hipoteseis nula")
    else:
        print("No se puede rechazar la hipotesis nula")
    