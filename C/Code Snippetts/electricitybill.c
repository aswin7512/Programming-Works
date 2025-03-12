/*program to calculate electricity bill*/
#include<stdio.h>
void main()
{
    int a,b,t;
    printf("ENTER CONSUMER NUMBER AND CONSUMPTION: ");
    scanf("%d %d", &a,&b);
    if (b<100)
    {
        t=3*b;
    }
    else if (b<200)
    {
        t=3*100+5*(b-100);
    }
    else
    {
        t=3*100+5*100+10*(b-200);
    }
    printf("BILL AMOUNT=%d",t);
}