/*program to find the average of 4 numbers*/
#include<stdio.h>
void main()
{
    float a,b,c,d,avg;
    printf("ENTER 4 NUMBERS: ");
    scanf("%f %f %f %f",&a,&b,&c,&d);
    avg=(a+b+c+d)/4.0;
    printf("AVERAGE=%f",avg);
}