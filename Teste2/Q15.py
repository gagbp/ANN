'''

Use um método de Runge-Kutta de ordem 4 para aproximar a solução do pvi.

y′=3.88y(1−x)+2.73x+1.22,y(1.16)=2.82.

Use tamanho do passo h=0.125 e realize 10 iterações.

'''
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
# y' = 3.88*y*(1 - x) + 2.73 * x + 1.22, y(1.16) = 2.82
# possui única solução pelo EXU

x0, y0 = 2.04, 1.12
h = 0.125 # tamanho do passo
n = 11

def f(x, y):
    return 3.73*y*(1 - x) + 1.73 * x + 1.89

def solucao_do_pvi(x):
    return np.e**x*(2.34 - 1.17*x)

def rk4(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h / 2, y[k] + m1 * h / 2)
        m3 = f(x[k] + h / 2, y[k] + m2 * h / 2)
        m4 = f(x[k] + h, y[k] + m3 * h)
        y[k + 1] = y[k] + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4) # <- fórmula do método de Runge-Kutta
    return x, y

xs, ys = rk4(f, x0, y0, h, n)
x = [v for _, v in xs.items()]
y = [v for _, v in ys.items()]

t = np.linspace(x0, x0 + n * h, 100)

for i in range(len(y)):
    print("y{} = {}".format(i,y[i]))

plt.scatter(x, y, label="Runge-Kutta de ordem 4")
plt.plot(t, solucao_do_pvi(t))
plt.legend()
plt.show()
