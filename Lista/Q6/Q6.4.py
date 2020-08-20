import numpy as np

pontos = [(-2.5,-5.6), (-2.0,-4.03), (-1.5,-0.4), (-1.0,-1.12), (-0.5,1.51), (0.0,2.98), (0.5,-4.59), (1.0,0.56), (1.5,-4.43),(2.0,-5.53), (2.5,2.14), (3.0,4.02), (3.5,0.85), (4.0,1.37), (4.5,5.26), (5.0,2.79), (5.5,5.16), (6.0,-2.28), (6.5,-2.9), (7.0,-0.61), (7.5,-3.93), (8.0,2.04), (8.5,5.61), (9.0,-2.09), (9.5,1.55), (10.0,-0.59), (10.5,-5.47), (11.0,-5.5),(11.5,2.64), (12.0,2.0), (12.5,5.1)]
n = len(pontos)
def vandermond(pontos):
    xs, ys = zip(*pontos)
    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    a = np.linalg.solve(A, B)
    return a

a = vandermond(pontos)

def p(x):
    px = sum([a[k] * x ** k for k in range(n)])
    return px

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

def equation(pontos):
    eq = ""
    eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq

eq = equation(pontos)
print(eq)

# obs esse é o mesmo polinômio que o polinômio de Lagrange

import matplotlib.pyplot as plt
import numpy as np

def poly_f(x):
    return eval(eq)

xs, ys = zip(*pontos)
a, b = min(xs) - 0.5, max(xs) + 0.5
t = np.arange(a, b, 0.01)
plt.scatter(xs, ys)
plt.plot(t, poly_f(t), color="red", label="polinômio interpolador")
plt.show()