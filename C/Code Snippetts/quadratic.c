//TO FIND ROOT OF QUADRATIC EQN
#include<stdio.h>          //ax2+bx+c=0
#include<math.h>
int main(){
    float a,b,c,d,r1,r2;
    printf("ENTER a,b,c: ");
    scanf("%f %f %f",&a,&b,&c);
    d=(b*b)-(4*a*c);
    if (d==0){
        printf("ROOTS ARE REAL AND SAME\n");
        r1=-b/(2*a);
        printf("ROOT IS %f",r1);
    }
    else if (d>0){
        printf("ROOTS ARE REAL AND DISTINCT\n");
        r1=(-b+sqrt(d))/(2*a);
        r2=(-b-sqrt(d))/(2*a);
        printf("ROOT 1: %f\nROOT 2: %f");
    }
    else{
        printf("ROOTS ARE IMAGINARY\n");
        r1=-b/(2*a);
        r2=sqrt(-d)/(2*a);
        printf("ROOT 1: %f + %fi\nROOT 2: %f - %fi",r1,r2,r1,r2);
    }
    return 0;
}