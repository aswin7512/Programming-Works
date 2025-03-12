/*program to convert Fahrenheit to degree celsius*/
#include<stdio.h>
void main()
{
    float f,c;
    printf("ENTER FAHRENHEIT VALUE: ");
    scanf("%f",&f);
    c=(f-32.0)*5.0/9.0;
    printf("CELSIUS VALUE=%f",c);
}