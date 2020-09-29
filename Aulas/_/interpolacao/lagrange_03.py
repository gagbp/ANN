pontos = [(0.26, 6.279), (0.27, 5.981), (0.44, 5.496), (0.68, 5.537), (1.55, 7.058), (1.66, 6.552), (1.77, 6.406), (1.89, 7.71), (2.26, 6.885), (2.68, 7.473), (2.77, 8.454), (2.79, 7.647), (2.82, 7.224), (3.03, 7.384), (3.04, 7.925), (3.24, 7.556), (3.27, 8.128), (3.59, 8.006), (3.73, 8.613), (3.76, 9.773), (3.83, 9.539), (4.2, 9.895), (4.32, 10.395), (4.51, 8.739), (4.81, 9.968), (5.01, 9.428), (5.31, 10.727), (5.48, 10.258), (5.5, 10.085), (5.65, 10.795), (5.74, 10.57), (6.08, 10.932), (6.36, 11.376), (6.48, 10.544), (6.58, 11.84), (6.66, 12.334), (6.81, 11.477), (7.08, 12.537), (7.1, 11.473), (7.2, 11.093), (7.52, 12.912), (7.59, 11.82), (7.64, 11.46), (7.7, 11.732), (8.62, 13.715), (8.97, 14.27), (9.01, 13.65), (9.04, 13.701), (9.77, 14.38), (9.91, 13.637)]

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

def pl(x):
    return lagrange(pontos, x)

import matplotlib.pyplot as plt

# função para interpolar
def f(x):
    return 1 / (1 + 25 * x ** 2)

# usado para desenhar o gráfico da função
# pontos no intervalo [-1, 1]
t = [-1 + i * (2 / 999) for i in range(1000)]
ft = [f(i) for i in t]
plt.plot(t, ft, label="gráfico de $f(x)=\\frac{1}{1 + 25x^2}$")
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
pt = [pl(i) for i in t]
plt.plot(t, pt, label="polinômio interpolador")
plt.legend()
plt.title(f"{n} pontos")
# Fenômeno de Runge
# plt.savefig(f'{n}pontos', dpi=300)
plt.show()

