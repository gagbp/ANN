import math
import numpy as np
import sympy as sy

qnt_derivadas = 3

for i in range(qnt_derivadas):
    x0 = 1 # <- deriva neste ponto
    n = 4 # <- usa essa quantidade de pontos
    der = i+1 # <- deriva este tanto de vezes <- botar quantas vezes derivará
    h = 0.01
    xs = [h * (-1 + i*(2/(n-1))) + x0 for i in range(n)]
    print("calculando derivada de ordem", der)
    print("pontos:",xs)

    def f(x):
        #AQUI VOCÊ BOTA O POLINOMIO CASO SEJA TIPO A Q9 OU A FUNÇÃO CASO SEJA TIPO A Q8
        #return x**x
        #return np.cos(x)
        return np.e**x

    A = [[x ** i for x in xs] for i in range(n)]
    # print(A)

    B = []
    for i in range(n):
        if i < der:
            B.append(0)
        else:
            B.append(x0 ** (i - der) * math.factorial(i) / math.factorial(i - der))

    # print(B)
    c = np.linalg.solve(A, B)

    def formula(xs, c):
        soma = 0
        for i in range(n):
            soma += c[i] * f(xs[i])
        return soma

    der_f_em_x0 = formula(xs, c)
    print('aprox:', der_f_em_x0)

    x = sy.Symbol('x')
    string = 'x**x'
    F = sy.sympify(string)
    exact = sy.diff(F, x, der).subs(x, x0)
    print('exact:', exact.evalf())
    print("")