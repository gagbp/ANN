'''

Use o método de Heun para aproximar a solução do pvi.

y′=2.34y(1−x)+2.49x+0.78,y(0.74)=4.1.

Use tamanho do passo h=0.125 e realize 10 iterações.

'''
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
# y' = 2.34*y*(1−x) + 2.49*x + 0.78, y(0.74) = 4.1
# possui única solução pelo EXU

x0, y0 = 2.59, 3.21
h = 0.125 # tamanho do passo
n = 11

def f(x, y):
    return 1.12*y*(1 - x) + 1.15 * x + 0.91

def solucao_do_pvi(x):
    return np.e**x*(2.34 - 1.17*x)

def heun(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 2) * (m1 + m2) # <- fórmula do método de Heun
    return x, y

xs, ys = heun(f, x0, y0, h, n)
x = [v for _, v in xs.items()]
y = [v for _, v in ys.items()]

t = np.linspace(x0, x0 + n * h, 100)

for i in range(len(y)):
    print("y{} = {}".format(i,y[i]))

plt.scatter(x, y, label="Heun")
plt.plot(t, solucao_do_pvi(t))
plt.legend()
plt.show()
