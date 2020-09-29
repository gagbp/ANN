'''

Encontre os coeficientes da parabola y=a0+a1x+a2x2 que melhor se aproxima da seguinte lista de 50 pontos

[(-2.876, 3.392), (-2.786, 3.636), (-2.766, 3.842), (-2.756, 3.712), (-2.736, 3.708), (-2.726, 3.646), (-2.696, 3.437), (-1.996, 3.474), (-1.466, 3.521), (-1.196, 3.232), (-1.146, 3.352), (-1.066, 3.177), (-0.516, 3.182), (-0.466, 3.232), (-0.246, 2.921), (-0.196, 3.11), (-0.146, 3.309), (-0.126, 3.153), (-0.026, 3.175), (0.024, 3.231), (0.214, 3.363), (0.344, 3.111), (0.494, 3.165), (0.604, 3.213), (0.974, 2.922), (1.234, 2.829), (1.324, 3.153), (1.374, 3.086), (1.634, 3.126), (1.794, 3.213), (1.904, 3.219), (2.084, 2.938), (2.164, 3.281), (2.234, 3.16), (2.384, 2.904), (2.694, 2.831), (2.824, 2.908), (2.884, 3.115), (3.124, 3.319), (3.334, 3.08), (3.644, 3.281), (3.764, 2.979), (3.964, 3.329), (4.284, 3.165), (4.374, 3.494), (4.974, 3.113), (5.314, 3.356), (6.534, 3.759), (6.654, 3.511), (6.704, 3.865)]

'''
import math
import random as r
import matplotlib.pyplot as plt
import numpy as np

a,b = -3,7
entrada = [(-2.876, 3.392), (-2.786, 3.636), (-2.766, 3.842), (-2.756, 3.712), (-2.736, 3.708), (-2.726, 3.646), (-2.696, 3.437), (-1.996, 3.474), (-1.466, 3.521), (-1.196, 3.232), (-1.146, 3.352), (-1.066, 3.177), (-0.516, 3.182), (-0.466, 3.232), (-0.246, 2.921), (-0.196, 3.11), (-0.146, 3.309), (-0.126, 3.153), (-0.026, 3.175), (0.024, 3.231), (0.214, 3.363), (0.344, 3.111), (0.494, 3.165), (0.604, 3.213), (0.974, 2.922), (1.234, 2.829), (1.324, 3.153), (1.374, 3.086), (1.634, 3.126), (1.794, 3.213), (1.904, 3.219), (2.084, 2.938), (2.164, 3.281), (2.234, 3.16), (2.384, 2.904), (2.694, 2.831), (2.824, 2.908), (2.884, 3.115), (3.124, 3.319), (3.334, 3.08), (3.644, 3.281), (3.764, 2.979), (3.964, 3.329), (4.284, 3.165), (4.374, 3.494), (4.974, 3.113), (5.314, 3.356), (6.534, 3.759), (6.654, 3.511), (6.704, 3.865)]
n = 50
xs = [x for (x,y) in entrada]
ys = [y for (x,y) in entrada]

def f(x):
    aux = [y for (t,y) in entrada if t == x]
    return aux[0]


num = 3
fs = [f'x**{i}' for i in range(num)]
def simpson(f, a, b, intvals):
    h = (b - a) / intvals
    xs = [x for (x,y) in entrada]
    last = len(xs) - 1
    soma = f(xs[0]) + f(xs[last])
    soma += 2 * sum([f(xs[i]) for i in range(2, last, 2)])
    soma += 4 * sum([f(xs[i]) for i in range(1, last, 2)])
    return (h / 3) * soma

class BestFunc:
    # usa a regra de simpson para resolver as integrais no sistema

    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b

    def coeffs(self, functions, intvals=100):
        A = {} # a_ij = int_a^bfi*fjdx
        n = len(functions)
        for i in range(n):
            A[i] = {}
            for j in range(n):
                if i <= j:
                    def f_ij(x):
                        return eval(functions[i]) * eval(functions[j])
                    A[i][j] = simpson(f_ij, a, b, intvals)
                else:
                    A[i][j] = A[j][i]
        A = [[v for _, v in value.items()] for _, value in A.items()]

        B = []
        for i in range(n):
            def func(x):
                return f(x) * eval(functions[i])
            val = simpson(func, a, b, intvals)# int_a^b(f*fi)dx
            B.append(val)
        coeffs = np.linalg.solve(A, B)
        return coeffs

obj = BestFunc(f, a, b)

coeffs = obj.coeffs(fs, 200)

def s(x):
    if x < 0:
        return f' {x}'
    return f' + {abs(x)}'

combina = ''.join([f'{s(ci)}*{fi}' for ci, fi in zip(coeffs, fs)])
def g(x):
    return eval(combina)

print("y = {}".format(combina))

def erro(x):
    return (f(x) - g(x)) ** 2

err = simpson(erro, a, b, 200)

plt.scatter(xs, ys)

t = np.arange(a, b, 0.01)
gt = [g(x) for x in t]
plt.plot(t, gt, color='blue', label=f'erro = {err}')

plt.legend()
plt.show()
'''
y =  + 3.150405650797624*x**0 -0.10516460775534556*x**1 + 0.02754078948574469*x**2
[ 3.21057081e+00 -2.11130518e-02 -4.61713223e-01  1.30051089e-01
  4.39916209e-01 -2.27351099e-01 -9.22611820e-02  8.21795798e-02
 -5.16593453e-03 -9.24573272e-03  2.67353140e-03  3.87116880e-05
 -1.45366687e-04  2.95972969e-05 -2.58406696e-06  8.72134411e-08]
'''