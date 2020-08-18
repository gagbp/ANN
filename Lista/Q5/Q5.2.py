pontos = [(-2.5,-3.99), (-2.0,-5.26), (-1.5,0.54), (-1.0,-4.29), (-0.5,-2.59), (0.0,-0.95), (0.5,-0.15)]

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