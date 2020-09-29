'''

Use a regra de Simpson para aproximar o valor da integral ∫1.08364 −0.55554 e**−x**2 dx. Use o número n de subintervalos indicado.

'''
import math

exact = 1.27841

a, b = -0.55554, 1.08364
def f(x):
    return math.exp(-x ** 2)


def simpson(f, h, xs):
    last = len(xs) - 1
    soma = f(xs[0]) + f(xs[last])
    soma += 2 * sum([f(xs[i]) for i in range(2, last, 2)])
    soma += 4 * sum([f(xs[i]) for i in range(1, last, 2)])
    return (h / 3) * soma

for n in range(10):
    h = (b - a) / 2 ** n
    xs = [a + k * h for k in range(2 ** n + 1)]
    aprox = simpson(f, h, xs)
    print('qtde:', 2 ** n, 'aprox:', aprox, 'erro:', abs(exact - aprox))

'''
qtde: 1 aprox: 0.5701609624115984 erro: 0.7082490375884016
qtde: 2 aprox: 1.3042709011280522 erro: 0.02586090112805217
qtde: 4 aprox: 1.2792290011218217 erro: 0.0008190011218216497
qtde: 8 aprox: 1.2784559749627893 erro: 4.59749627892414e-05
qtde: 16 aprox: 1.2784111767391297 erro: 1.176739129693516e-06
qtde: 32 aprox: 1.278408428088148 erro: 1.5719118520163278e-06
qtde: 64 aprox: 1.2784082570825068 erro: 1.7429174932193092e-06
qtde: 128 aprox: 1.2784082464068602 erro: 1.7535931398082738e-06
qtde: 256 aprox: 1.278408245739822 erro: 1.7542601780107248e-06
qtde: 512 aprox: 1.278408245698136 erro: 1.7543018639987196e-06
'''