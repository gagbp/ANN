'''

Use o método de Ralston para aproximar a solução do pvi.

y′=2.53y(1−x)+2.14x+0.63,y(1.28)=1.03.

Use tamanho do passo h=0.125 e realize 10 iterações.

'''
import matplotlib.pyplot as plt
import numpy as np
# y' = 2.53y(1−x)+2.14x+0.63, y(1.28) = 1.03
# possui única solução pelo EXU

x0, y0 = 0.67,3.49
h = 0.125 # tamanho do passo
n = 11

def f(x, y):
    return 1.9*y*(1-x) + 1.18*x + 1.77

def solucao(x):
    return np.e**x*(2.53 - 1.265*x)

def ralston(f, x0, y0, h, n):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + (3/4)*h, y[k] + m1 * (3/4)*h)
        y[k + 1] = y[k] + (h / 3) * (1 * m1 + 2 * m2) # <- fórmula do método de Ralston
    return x, y

rxs, rys = ralston(f, x0, y0, h, n)
rx = [v for _, v in rxs.items()]
ry = [v for _, v in rys.items()]

for i in range(len(ry)):
    print("y{} = {}".format(i,ry[i]))

t = np.linspace(x0, x0 + n * h, 100)

plt.scatter(rx, ry, label="Ralston")
plt.plot(t, solucao(t))
plt.legend()
plt.show()
'''
y0 = 1.03
y1 = 1.3368042531683595
y2 = 1.5881204035192216
y3 = 1.773405324712674
y4 = 1.8909379426440138
y5 = 1.9465132030262926
y6 = 1.9510585734926642
y7 = 1.9179001788655372
y8 = 1.860326013908565
y9 = 1.7898556926161244
y10 = 1.7153434777022205
'''