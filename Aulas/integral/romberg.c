#include<math.h>
#include<stdio.h>
//exact = 0.74682413281242725399467436131853005354499686812606329027654
//integral exp(-x^2) x=0..1

//escrever a regra dos trapézio para a função f: F1
double f(double x) {
    return exp(-x * x);
}

double F1(double h){
    double a = 0, b = 1;
    double n = (b-a)/h;
    double aprox = 0;

    for (double i = 1; i < n; i++){
        double xi = a + h * i;
        aprox += f(xi);
    }
    

    return (h/2) * (f(a) + 2*aprox + f(b));
}

double mod(double x){
    if (x<0){
        return -x;
    }else
    {
        return x;
    }
}

double Fk(double h, double k){
    if(k==1)
        return F1(h);
    k -= 1;
    return (pow(2,2*k) * Fk(h/2, k) - Fk(h, k)) / (pow(2,2*k) - 1);
}

int main(){
    double h = 1/4;
    int k = 4; //com isso o erro será de ordem 2*(k+1)
    double t = F1(h);
    double r = Fk(h,k);
    double exact = 0.746824132812;
    printf("aprox: %10.16lf \t exact:%10.16lf\n", t, mod(exact - t));
    printf("aprox: %10.16lf \t exact:%10.16lf\n", r, mod(exact - r));
    return 0;
}