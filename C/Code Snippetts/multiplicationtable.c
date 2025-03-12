/*program to prepare multiplication table*/
#include<stdio.h>
void main()
{
    int a,i;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    for(i=1;i<=10;i++)
    {
        printf("%d * %d = %d\n",i,a,i*a);
    }
}