/*program to find the roots of a quadratic equation*/
#include<stdio.h>
#include<math.h>
void main()
{
    float a,b,c,r1,r2,d,k;
    printf("ENTER a, b and c: ");
    scanf("%f %f %f",&a,&b,&c);
    d=b*b-4*a*c;
    printf("%f",d);
    if (d==0)
    {
        printf("ROOTS ARE REAL AND SAME\n");
        r1=-b/(2*a);
        printf("ROOT IS: %.2f",r1);
    }
    else if (d>0)
    {
        printf("ROOTS ARE REAL AND DISTINCT\n");
        r1=(-b+sqrt(d))/(2*a);
        r2=(-b-sqrt(d))/(2*a);
        printf("ROOT 1: %.2f\nROOT 2: %.2f",r1,r2);
    }
    else
    {
        printf("ROOTS ARE IMAGINARY\n");
        r1=-b/(2*a);
        k=-b;
        r2=sqrt(k)/(2*a);
        printf("ROOT 1: %.2f\nROOT 2: %.2f",r1,r2);
    }
}