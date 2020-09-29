import random as r
import matplotlib.pyplot as plt
import numpy as np

# modelo de pontos
a, b = -2,2
n = 100
xs = [a + r.random() for _ in range(n)]
num = 2
data_coefs = [-2 + 4 * r.random() for _ in range(num)]
def data(x):
    # a + b * x + erro
    erro = r.random() / 10
    val = sum(c ** x ** i for i, c in enumerate(data_coefs)) + erro
    return val
ys = [data(x) for x in xs]


def min_q(pontos):
    n = len(pontos)
    sumxk = sum(x for x, _ in pontos)
    sumxk2 = sum(x ** 2 for x, _ in pontos)
    sumyk = sum(y for _, y in pontos)
    sumykxk = sum(x * y for x, y in pontos)
    A = [[n, sumxk], [sumxk, sumxk2]]
    B = [sumyk, sumykxk]
    coefs = np.linalg.solve(A,B)
    return coefs # a0 e a1

def least_squares(pontos, k):
    n = len(pontos)
    A = {}
    B = {}
    for i in range(n):
        A[i] = {}
        for j in range(n):
            if j >= i:
                A[i][j] = sum(x**(i+j) for x, _ in pontos)
            else:
                A[j][i] = A[i][j]
    A = [[A[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        B.append(sum(y*x**i for x, y in pontos))
    coefs = np.linalg.solve(A, B)

pontos = list(zip(xs, ys))
c = min_q(pontos)
print(c)

def fit_poly(x):
    return sum(c * x **i for i, c in enumerate(c)) # c[0] * x**0 + c[1] * x **1
