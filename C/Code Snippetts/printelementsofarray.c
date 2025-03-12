/*program to print the elements of an array*/
#include<stdio.h>
void main()
{
    int a[10],i;
    for(i=10;i<10;i++)
    {
        printf("ENTER NUMBER %d",i+1);
        scanf("%d",&a[i]);
    }
    printf("10 NUMBERS ARE\n");
    for(i=0;i<10;i++)
    {
        printf("%d\n",a[i]);
    }
}