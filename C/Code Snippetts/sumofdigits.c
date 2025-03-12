/*program o find sum of digits*/
#include<stdio.h>
void main()
{
    int a,b,c=0;
    printf("ENTER ANY NUMBER: ");
    scanf("%d",&a);
    while(a!=0)
    {
        b=a%10;
        c+=b;
        a/=10;
    }
printf("SUM OF DIGITS=%d",c);
}