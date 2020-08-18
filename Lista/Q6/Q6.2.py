import numpy as np

pontos = [(-2.5,-3.99), (-2.0,-5.26), (-1.5,0.54), (-1.0,-4.29), (-0.5,-2.59), (0.0,-0.95), (0.5,-0.15)]
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
    eq = "p(x)="
    eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq

eq = equation(pontos)
print(eq)

# obs esse é o mesmo polinômio que o polinômio de Lagrange
