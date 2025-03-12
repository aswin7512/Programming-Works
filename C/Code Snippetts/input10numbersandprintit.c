/*program to input 10 numbers to and array using array of pointer and print it*/
#include<stdio.h>
void main()
{
    int a[10],i;
    int *pi[10];
    printf("ENTER ");
    for(i=0;i<10;i++)
    {
        printf("ELEMENT %d: ",i);
        scanf("%d",&a[i]);
        pi[i]=&a[i];
    }
    printf("THE ELEMENTS ENTERED ARE\n");
    for(i=0;i<10;i++)
    {
        printf("%d\n",*pi[i]);
    }
}