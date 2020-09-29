'''

se o método de Euler para aproximar a solução do pvi.

y′=3.47y(1−x)+1.72x+1.96,y(0.39)=1.36.

Use tamanho do passo h=0.125 e realize 10 iterações.

'''
import matplotlib.pyplot as plt
import numpy as np
# y' = 3.47*y*(1-x) + 1.72*x + 1.96, y(0.39) = 1.36
# possui única solução pelo EXU

x0, y0 = 0.39, 1.36
h = 0.125 # tamanho do passo
n = 11

def f(x, y):
    return 3.47*y*(1 - x) + 1.72 * x + 1.96

def solucao_do_pvi(x):
    return np.e**x*(3.47 - 1.735*x)

def euler(f, x0, y0, h, n):
    x = {0: x0}
    y = {0: y0}
    for i in range(1, n):
        x[i] = x0 + i * h # <- listando os pontos na partição
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h # <- fórmula do método
    return x, y

xs, ys = euler(f, x0, y0, h, n)
x = [v for _, v in xs.items()]
y = [v for _, v in ys.items()]

t = np.linspace(x0, x0 + n * h, 100)

for i in range(len(y)):
    print("y{} = {}".format(i,y[i]))

plt.scatter(x, y, label="Euler")
plt.plot(t, solucao_do_pvi(t))
plt.legend()
plt.show()
