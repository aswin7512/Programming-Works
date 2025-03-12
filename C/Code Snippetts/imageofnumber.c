/*program to print image of a number*/
#include<stdio.h>
void main()
{
    int a,b;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    while(a!=0)
    {
        b=a%10;
        a/=10;
        printf("%d",b);
    }
}