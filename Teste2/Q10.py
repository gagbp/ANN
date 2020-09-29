'''
Sejam
f1(x)=1, f2(x)=x1, f3(x)=x2, f4(x)=x3, f5(x)=x4, f6(x)=x5
Encontre os coeficientes da combinação linear

f(x)≃a1f1(x)+a2f2(x)+a3f3(x)+a4f4(x)+a5f5(x)+a6f6(x)

que melhor se aproxima da função f(x)=2sin(x)+cos(x) no intervalo [−0.838,0.946].
Para o cálculo das integrais use a regra dos Trapézios com n=128. subintervalos.

'''
import numpy as np
import matplotlib.pyplot as plt

a, b = -0.838, 0.946

def f(x):
    return 2*np.sin(x) + np.cos(x)

num = 6
fs = [f'x**{i}' for i in range(num)]

def simpson(f, a, b, intvals):
    h = (b - a) / intvals
    xs = [a + i * h for i in range(intvals + 1)]
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

coeffs = obj.coeffs(fs, 128)

def s(x):
    if x < 0:
        return f'{x}'
    return f'+{abs(x)}'

combina = ''.join([f'{s(ci)}*{fi}' for ci, fi in zip(coeffs, fs)])
def g(x):
    return eval(combina)

print(combina)

def erro(x):
    return (f(x) - g(x)) ** 2

err = simpson(erro, a, b, 128)

t = np.arange(a, b, 0.01)
ft = [f(x) for x in t]
gt = [g(x) for x in t]
plt.plot(t, ft, 'r')
plt.plot(t, gt, color='blue', label=f'erro = {err}')
plt.legend()
plt.show()
