pontos = [(-2.5,0.94), (-2.0,-3.08), (-1.5,5.33), (-1.0,2.57), (-0.5,-5.94), (0.0,4.39), (0.5,-2.35), (1.0,0.17), (1.5,5.38),(2.0,-1.13), (2.5,-2.63)]

def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def lagrange(pontos, x):
    # retorna o valor do polinômio de Lagrange que interpola
    # a lista 'pontos' calculado no ponto x
    xs, ys = zip(*pontos)
    soma = 0
    for k, y in enumerate(ys):
        xk = xs[k]
        Lk_numerador = prod([x - xi for i, xi in enumerate(xs) if i != k])
        Lk_denominador = prod([xk - xi for i, xi in enumerate(xs) if i != k])
        soma += y * (Lk_numerador / Lk_denominador)
    return soma

def p(x):
    return lagrange(pontos, x)

import matplotlib.pyplot as plt

# função para interpolar
def f(x):
    return 

# usado para desenhar o gráfico da função
# pontos no intervalo [-1, 1]
t = [-1 + i * (2 / 999) for i in range(1000)]
ft = [f(i) for i in t]
plt.plot(t, ft, label="gráfico de $f(x)")
# plt.show()

# polinômio interpolador
# lista de pontos no intervalo [-1, 1]
n = 20
xs = [-1 + i * (2 / (n - 1)) for i in range(n)]
ys = [f(i) for i in xs]
pontos = [(x, f(x)) for x in xs]

# plotar os 'pontos'
plt.scatter(xs, ys)

# plotar o gráfico de p(x)
pt = [p(i) for i in t]
plt.plot(t, pt, label="polinômio interpolador")
plt.legend()
plt.title(f"{n} pontos")
# Fenômeno de Runge
# plt.savefig(f'{n}pontos', dpi=300)
plt.show()