'''

Encontre os coeficientes do polinômio de grau 3 y=a0+a1x+a2x2+a3x3 que melhor se aproxima da seguinte lista de 50 pontos

[(-1.856, 0.94), (-1.832, 1.046), (-1.704, 2.096), (-1.664, 2.197), (-1.344, 4.011), (-1.216, 4.631), (-0.984, 5.148), (-0.896, 5.554), (-0.824, 5.749), (-0.816, 5.723), (-0.776, 5.418), (-0.744, 5.812), (-0.696, 5.852), (-0.56, 5.456), (-0.368, 5.581), (-0.304, 5.636), (-0.28, 5.622), (-0.24, 5.564), (-0.192, 5.578), (-0.152, 5.38), (-0.096, 5.312), (0.008, 5.265), (0.04, 5.126), (0.08, 5.086), (0.152, 5.175), (0.168, 5.229), (0.2, 4.812), (0.232, 4.94), (0.288, 4.876), (0.304, 5.031), (0.4, 5.007), (0.44, 4.709), (0.48, 5.106), (0.496, 4.773), (0.816, 5.202), (0.872, 5.199), (1.008, 5.456), (1.248, 5.945), (1.288, 6.145), (1.328, 6.399), (1.368, 6.544), (1.392, 6.51), (1.408, 6.825), (1.448, 6.948), (1.544, 7.558), (1.608, 7.558), (1.672, 8.389), (1.776, 9.077), (1.8, 9.203), (1.808, 9.358)]


'''
import math
import random as r
import matplotlib.pyplot as plt
import numpy as np

a,b = -2,2
entrada = [(-1.856, 0.94), (-1.832, 1.046), (-1.704, 2.096), (-1.664, 2.197), (-1.344, 4.011), (-1.216, 4.631), (-0.984, 5.148), (-0.896, 5.554), (-0.824, 5.749), (-0.816, 5.723), (-0.776, 5.418), (-0.744, 5.812), (-0.696, 5.852), (-0.56, 5.456), (-0.368, 5.581), (-0.304, 5.636), (-0.28, 5.622), (-0.24, 5.564), (-0.192, 5.578), (-0.152, 5.38), (-0.096, 5.312), (0.008, 5.265), (0.04, 5.126), (0.08, 5.086), (0.152, 5.175), (0.168, 5.229), (0.2, 4.812), (0.232, 4.94), (0.288, 4.876), (0.304, 5.031), (0.4, 5.007), (0.44, 4.709), (0.48, 5.106), (0.496, 4.773), (0.816, 5.202), (0.872, 5.199), (1.008, 5.456), (1.248, 5.945), (1.288, 6.145), (1.328, 6.399), (1.368, 6.544), (1.392, 6.51), (1.408, 6.825), (1.448, 6.948), (1.544, 7.558), (1.608, 7.558), (1.672, 8.389), (1.776, 9.077), (1.8, 9.203), (1.808, 9.358)]
n = 50
xs = [x for (x,y) in entrada]
ys = [y for (x,y) in entrada]

def f(x):
    aux = [y for (t,y) in entrada if t == x]
    return aux[0]


num = 4
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



# método dos minimos quadrados geral
def least_squares(pontos, k): # se k == 1, então o resultado é o mesmo de min_q(pontos)
    # vamos obter um sistema (k+1)x(k+1)
    n = len(pontos)
    A = {}
    B = []
    for i in range(k + 1):
        A[i] = {}
        for j in range(k + 1):
            if j >= i:
                A[i][j] = sum(x ** (i + j) for x, _ in pontos)
            else:
                A[i][j] = A[j][i]
    A = [[A[i][j] for j in range(k + 1)] for i in range(k + 1)]
    for i in range(k + 1):
        B.append(sum(y * x ** i for x, y in pontos))
    coefs = np.linalg.solve(A, B)
    return coefs

pontos = list(zip(xs, ys))
c = least_squares(pontos, k=15)
print(c)

def fit_poly(x):
    return sum(c * x ** i for i, c in enumerate(c)) # sum c[j] * x ** j, j=0,1,2,...,k

erro = sum((y - fit_poly(x)) ** 2 for x, y in pontos)
tq = np.arange(a, b, 0.01)



plt.scatter(xs, ys)

h = (b - a) / n
ta = [a + i * h for i in range(n)]

t = np.arange(a, b, 0.01)
gt = [g(x) for x in t]
plt.plot(t, gt, color='blue', label=f'erro = {err}')

plt.plot(tq, fit_poly(t), 'g', label=f"erro = {erro}")

plt.legend()
plt.show()
'''
y =  + 5.280325095206693*x**0 -0.9937524930263245*x**1 + 0.0009544502917067964*x**2 + 0.9949278530901715*x**3
[ 5.26347865 -1.30311391 -0.54653841  2.727182    4.48659155 -2.73599937
 -8.71503823  1.59056282  7.39863594  0.00960836 -3.16932531 -0.35468861
  0.6734696   0.12689632 -0.05648136 -0.01385285]
'''