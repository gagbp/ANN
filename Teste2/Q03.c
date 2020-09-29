/*

Os seguintes valores
F1(h/1)=0.8574205187061456, F1(h/2)=1.121611060991343, F1(h/4)=1.1753375246731685, F1(h/8)=1.1883354607968923, F1(h/16)=1.1915597539668552
são aproximações para o valor da integral ∫0.75−0.64e−x2dx obtidas usando a regra dos trapézios. Use o método de Romberg para obter uma aproximação para o valor dessa integral com erro O(h10) a partir das aproximações acima.

*/
#include <math.h>
#include <stdio.h>

// exact = 0.7468241328124270253994674361318530053544996868126063290276544989586053275617728314978484298229019197;
// integral exp(-x^2) x=0..1

// escrever a regra dos trapézios para a função f: F1
double F1(double h) {
    // aqui você pode modificar
    double a = -0.64, b = 0.75;
    double n = (b - a) / h;
    double f(double x) {
        return exp(- x * x);
    }
    // não modifique
    double aprox = 0.0;
    for (int i = 1; i < n; i++) {
        double xi = a + h * i;
        aprox += f(xi);
    }
    return (h / 2) * (f(a) + 2 * aprox + f(b));
}

double mod(double x) {
    if (x < 0)
        return -x;
    return x;
}
//formula de Romberg: Fk

double Fk(double h, double k) {
    if (k == 1)
        return F1(h);
    k -= 1;
    return (pow(2, 2 * k) * Fk(h / 2, k) - Fk(h, k)) / (pow(2, 2 * k) - 1);
}

int main() {
    double h = 1 / pow(2, 2);
    int k = 4; // com isso o erro será de ordem 2 * (k + 1)
    double t = F1(h);
    double r = Fk(h, k);
    double exact = 0.746824132812;
    printf("aprox: %10.16lf \t erro: %10.16lf\n", t, mod(exact - t));
    printf("aprox: %10.16lf \t erro: %10.16lf\n", r, mod(exact - r));
    return 0;
}

/*
aprox: 1.2530118679927178        erro: 0.5061877351807178
aprox: 1.1950387181340001        erro: 0.4482145853220001
*/