'''

Encontre os coeficientes da reta y=a0+a1x que melhor se aproxima da seguinte lista de 50 pontos

[(0.26, 6.279), (0.27, 5.981), (0.44, 5.496), (0.68, 5.537), (1.55, 7.058), (1.66, 6.552), (1.77, 6.406), (1.89, 7.71), (2.26, 6.885), (2.68, 7.473), (2.77, 8.454), (2.79, 7.647), (2.82, 7.224), (3.03, 7.384), (3.04, 7.925), (3.24, 7.556), (3.27, 8.128), (3.59, 8.006), (3.73, 8.613), (3.76, 9.773), (3.83, 9.539), (4.2, 9.895), (4.32, 10.395), (4.51, 8.739), (4.81, 9.968), (5.01, 9.428), (5.31, 10.727), (5.48, 10.258), (5.5, 10.085), (5.65, 10.795), (5.74, 10.57), (6.08, 10.932), (6.36, 11.376), (6.48, 10.544), (6.58, 11.84), (6.66, 12.334), (6.81, 11.477), (7.08, 12.537), (7.1, 11.473), (7.2, 11.093), (7.52, 12.912), (7.59, 11.82), (7.64, 11.46), (7.7, 11.732), (8.62, 13.715), (8.97, 14.27), (9.01, 13.65), (9.04, 13.701), (9.77, 14.38), (9.91, 13.637)]

'''
import math
import random as r
import matplotlib.pyplot as plt
import numpy as np

a,b = 0,10
entrada = [(0.05, 3.414), (0.45, 4.438), (0.61, 3.735), (0.67, 3.851), (0.85, 5.345), (1.49, 4.698), (1.92, 5.42), (2.31, 6.314), (2.33, 6.428), (2.43, 7.46), (2.46, 7.843), (2.6, 7.847), (3.07, 8.331), (3.38, 9.175), (3.4, 8.344), (3.8, 10.2), (3.81, 9.459), (4.02, 10.211), (4.3, 10.501), (4.41, 9.705), (4.53, 9.644), (4.69, 10.827), (4.73, 11.712), (4.77, 11.63), (5.28, 11.53), (5.29, 12.496), (5.44, 12.77), (5.98, 12.327), (5.99, 12.519), (6.05, 13.338), (6.25, 13.939), (6.64, 14.001), (6.82, 14.666), (6.93, 15.344), (6.99, 14.273), (7.06, 14.83), (7.56, 15.309), (7.74, 15.651), (7.8, 16.224), (8.29, 17.356), (8.3, 17.049), (8.51, 18.102), (8.71, 18.225), (8.84, 18.678), (9.47, 19.693), (9.51, 18.105), (9.57, 18.084), (9.67, 19.295), (9.89, 18.928), (9.95, 18.715)]
n = 50
xs = [x for (x,y) in entrada]
ys = [y for (x,y) in entrada]

def f(x):
    aux = [y for (t,y) in entrada if t == x]
    return aux[0]


# x --> x_til = ln(x)
xs_new = [math.log(x) for x in xs]
# y --> y_til = ln(y)
ys_new = [math.log(y) for y in ys]
pontos = list(zip(xs_new, ys_new))

# método dos mínimos quadrados para retas
def min_q(pontos):
    n = len(pontos)
    sumxk = sum(x for x, _ in pontos)
    sumxk2 = sum(x ** 2 for x, _ in pontos)
    sumyk = sum(y for _, y in pontos)
    sumykxk = sum(x * y for x, y in pontos)
    A = [[n, sumxk], [sumxk,sumxk2]]
    B = [sumyk, sumykxk]
    coefs = np.linalg.solve(A, B)
    return coefs # a0 e a1

# y_til = a_0 + a_1 + x_til
coefs = min_q(pontos) # [a0, a1]
# def p(x): # <-- a melhor reta
#     # a0 + ai * x
#     return sum(c * x ** i for i, c in enumerate(coefs))

a_ = math.exp(coefs[0])
b_ = coefs[1]
print("y = {} + {}*x".format(a_, b_))

def expo(x): # y = a * exp(b * x) # é a melhor função exponencial
    return a_ * math.exp(b_ * x)

def poten(x): # y = a * x ** b # é a melhor função potência
    # sensível demais ;(
    return a_ * x ** b_


num = 2
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
yt = [poten(x) for x in ta]
plt.plot(ta, yt, 'r')

t = np.arange(a, b, 0.01)
gt = [g(x) for x in t]
plt.plot(t, gt, color='blue', label=f'erro = {err}')

plt.plot(tq, fit_poly(t), 'g', label=f"erro = {erro}")

plt.legend()
plt.show()
'''
5.315338055366292 0.9171562616134854
'''