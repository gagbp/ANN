import numpy as np

pontos = [(-2.5,0.94), (-2.0,-3.08), (-1.5,5.33), (-1.0,2.57), (-0.5,-5.94), (0.0,4.39), (0.5,-2.35), (1.0,0.17), (1.5,5.38),(2.0,-1.13), (2.5,-2.63)]
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
