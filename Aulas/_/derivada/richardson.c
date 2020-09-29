#include<math.h>
#include<stdio.h>

/* 
    Nao ta funcionando
*/

double Fk(double h, double k){
    double F1h[] = {1.423425, 1.547362, 1.553842, 1.559343};
    if(k==1)
        return F1h[1];
    k -= 1;
    return (pow(2,1*k) * Fk(h/2, k) - Fk(h, k)) / (pow(2,1*k) - 1);
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