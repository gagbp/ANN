'''

Use a regra dos trapézios para aproximar o valor da integral ∬Re−(x+y)2dxdy, onde R=[−0.97,0.98]×[−0.71,0.91]. Particione o intervalo [−0.97,0.98] em n1=32 subintervalos e o intervalo [−0.71,0.91] em n2=48 subintervalos.

'''
import math
import numpy as np

def f(x, y):
    return np.e**(-1*(x+y)**2)

a, b = -0.97, 0.98
n1 = 32 # na regra de simpson a quantidade de pontos na partição tem que ser ímpar
c, d = -0.71, 0.91
n2 = 48 # na regra de simpson a quantidade de pontos na partição tem que ser ímpar
# WolframAplha digite "Integrate[e^(-1*(x+y)^2), {x, −0.97, 0.98}, {y, −0.71, 0.91}]" (sem aspas)
exact = 2.13113



def integral_dupla(f, a, b, c, d, n1, n2):
    if n1 < 2 or n2 < 2:
        raise ValueError("Me recuso a fazer contas com esses valores!")
    # partição do intervalo [a,b]
    h1 = (b - a) / (n1 - 1)
    xs = [a + h1 * i for i in range(n1)]
    # partição do intervalo [c, d]
    h2 = (d - c) / (n2 - 1)
    ys = [c + h2 * j for j in range(n2)]
    aprox = 0
    # pontos internos do retângulo R
    # for x in xs[1:-1]:
    #     for y in ys[1:-1]:
    #         approx += 4 * f(x, y)
    aprox += 4 * sum(f(x, y) for x in xs[1:-1] for y in ys[1:-1])

    # pontos internos das arestas de R
    aprox += 2 * sum(f(x, y) for x in [a, b] for y in ys[1:-1]) # arestas verticais
    aprox += 2 * sum(f(x, y) for x in xs[1:-1] for y in [c, d]) # arestas horizontais

    # pontos no vértice de R
    aprox += sum(f(x, y) for x in [a, b] for y in [c, d])
    return (h1 * h2 / 4) * aprox


def integral_dupla_s(f, a, b, c, d, n1, n2):
    if n1 % 2 != 1 or n2 % 2 != 1:
        raise ValueError('n1 e n2 têm que ser ímpares')
    if n1 < 2 or n2 < 2:
        raise ValueError("Me recuso a fazer contas com esses valores!")
    # partição do intervalo [a,b]
    h1 = (b - a) / (n1 - 1)
    xs = [a + h1 * i for i in range(n1)]
    # partição do intervalo [c, d]
    h2 = (d - c) / (n2 - 1)
    ys = [c + h2 * j for j in range(n2)]
    aprox = 0
    # centros dos sub-retângulos de R
    aprox += 16 * sum(f(xs[i], ys[j]) for i in range(1, n1, 2) for j in range(1, n2, 2))
    # vértices internos dos sub-retêngulos
    aprox += 4 * sum(f(xs[i], ys[j]) for i in range(2, n1 - 1, 2) for j in range(2, n2 - 1, 2))
    # pontos na aresta de R que são pontos médios da arestas de Rij
    aprox += 4 * sum(f(x, ys[j]) for x in [a, b] for j in range(1, n2, 2))
    aprox += 4 * sum(f(xs[i], y) for i in range(1, n1, 2) for y in [c, d])
    # pontos médios de vértices dos sub-retângulos
    aprox += 8 * sum(f(xs[i], ys[j]) for i in range(2, n1 - 1, 2) for j in range(1, n2 - 1, 2))
    aprox += 8 * sum(f(xs[i], ys[j]) for i in range(1, n1 - 1, 2) for j in range(2, n2 - 1, 2))
    # pontos nas arestas de R que são vértices de Rij
    aprox += 2 * sum(f(x, ys[j]) for x in [a,b] for j in range(2, n2 - 1, 2))
    aprox += 2 * sum(f(xs[i], y) for i in range(2, n2 - 1, 2) for y in [c, d])
    # vértics de R
    aprox += sum(f(x, y) for x in [a, b] for y in [c, d])

    return (h1 * h2 / 9) * aprox

i = integral_dupla(f, a, b, c, d, n1, n2)
print(f"aprox: {i}\nexact: {exact}\nerro: {abs(i - exact)}")
'''
aprox: 2.1303466889318297
exact: 2.13113
erro: 0.0007833110681705335
'''